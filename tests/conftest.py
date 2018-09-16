import pytest
import webdriver_monkey_patch


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument('headless')
    return chrome_options
