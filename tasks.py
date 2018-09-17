from invoke import task
from subprocess import Popen
import chromedriver_binary
import signal
import shutil


def start_app():
  return Popen(['pipenv', 'run', 'app'])

def start_chromedriver():
    return Popen([chromedriver_binary.chromedriver_filename, '--url-base=/wd/hub'])

pytest_base = 'pytest tests/webdriver --driver Remote --capability browserName Chrome --tests-per-worker 20 --sensitive-url "example.com"'

@task
def test(c, remote=False, url='http://localhost:8000'):
    try:
        app = start_app()
        if remote:
            driver = None
            c.run(pytest_base + ' --remote --base-url ' + url)
        else:
            driver = start_chromedriver()
            c.run(pytest_base + ' --host localhost --port 9515 --base-url ' + url)
    finally:
        if driver:
            driver.send_signal(signal.SIGINT)
            driver.wait()
        if app:
            app.send_signal(signal.SIGINT)
            app.wait()
