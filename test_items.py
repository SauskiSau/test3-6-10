import time
from selenium.webdriver.common.by import By


def test_add_to_cart_button_presence(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Добавьте sleep для визуальной проверки языка
    time.sleep(30)

    # Проверка наличия кнопки добавления в корзину
    add_to_basket_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert add_to_basket_button.is_displayed()
