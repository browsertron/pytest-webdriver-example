import time
import requests
from selenium.webdriver.remote.errorhandler import ErrorCode
from selenium.webdriver.remote.remote_connection import RemoteConnection
from urllib import parse


def threadsafe_request(self, method, url, body=None, retries=0):
    parsed_url = parse.urlparse(url)
    headers = self.get_remote_connection_headers(parsed_url, self.keep_alive)
    
    # reuse requests Session for keep_alive
    if self.keep_alive:
        self._session = self._session if hasattr(self, '_session') else requests.Session()
        req = self._session.request
    else:
        req = requests.request
    
    # do up to 3 retries for connection errors
    try:
        resp = req(method, url, headers=headers, data=body.encode('utf-8'))
    except requests.exceptions.ConnectionError as e:
        if retries < 3:
            time.sleep(0.015)
            retries += 1
            return threadsafe_request(self, method, url, body, retries)
        raise e
    
    if 200 <= resp.status_code < 300:
        return resp.json()
    elif 300 <= resp.status_code < 304:
        return self.threadsafe_request('GET', resp.headers['location'])
    elif 400 <= resp.status_code <= 500:
        status = resp.status_code
    else:
        status = ErrorCode.UNKNOWN_ERROR

    return {'status': status, 'value': resp.text.strip()}

RemoteConnection._request = threadsafe_request
