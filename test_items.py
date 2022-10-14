from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
selector = '.add-to-basket .btn-add-to-basket'
wait_time = 5


def test_check_exist_button(browser):
    browser.get(link)

    try:
        button = WebDriverWait(browser, wait_time).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, selector)))
    except TimeoutException:
        button = None

    assert button is not None, "-----Urri, Urri! Where is his button?------\n" \
                               "---Where is the button? Where is the button? I wish I knew where...---"

