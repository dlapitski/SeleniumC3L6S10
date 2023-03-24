from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_basket_button_exists(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    add_to_basket = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket1')
    assert len(add_to_basket) > 0, 'Could NOT find the "Add to basket" button'
    time.sleep(5)  # To check the correctness of the set language
