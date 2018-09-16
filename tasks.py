from invoke import task
from subprocess import Popen
import chromedriver_binary
import signal
import shutil


def start_app():
  return Popen(['pipenv', 'run', 'app'])

def start_chromedriver():
    return Popen([chromedriver_binary.chromedriver_filename, '--url-base=/wd/hub'])

@task
def test(c):
    app = start_app()
    driver = start_chromedriver()
    try:
        c.run('pytest tests/webdriver --driver Remote --port 9515 --capability browserName Chrome --tests-per-worker 20')
    finally:
        if driver:
            driver.send_signal(signal.SIGINT)
            driver.wait()
        if app:
            app.send_signal(signal.SIGINT)
            app.wait()
