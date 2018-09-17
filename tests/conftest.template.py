import pytest
import webdriver_monkey_patch
import os


def pytest_addoption(parser):
    group = parser.getgroup('selenium', 'selenium')
    group._addoption('--remote',
                     action='store_true',
                     help='run tests using grid defined by REMOTE_WEBDRIVER')


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument('headless')
    return chrome_options


@pytest.fixture
def driver_kwargs(driver_kwargs, pytestconfig):
    if pytestconfig.getoption('remote'):
        driver_kwargs['command_executor'] = os.environ['REMOTE_WEBDRIVER']
    return driver_kwargs
