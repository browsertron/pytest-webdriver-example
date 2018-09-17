from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_{{num}}(driver, base_url):
    driver.get(base_url)
    WebDriverWait(driver, 5).until(EC.title_is('Test Page'))
    assert driver.title == 'Test Page'    
