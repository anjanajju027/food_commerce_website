from pages.login import LoginPage
from pages.Homepage import HomePage
from pages.productpage import ProductPage
from pages.checkoutpage import CheckoutPage


def test_beelivery_flow(driver):
    driver.get("https://www.beelivery.com/#")

    login = LoginPage(driver)
    home = HomePage(driver)
    product = ProductPage(driver)
    checkout = CheckoutPage(driver)

    login.click_sign_in_link()
    login.login("anjanajju027@gmail.com", "Govindha10@")

    home.enter_postcode_and_order("SW1A 1AA")

    product.search_product("Cake")
    product.add_gourmet_gold()
    product.increase_quantity(2)

    assert product.verify_item_in_cart(), "Item not added in cart"

    checkout.select_delivery_slot()
    assert checkout.confirm_and_checkout(), "Did not navigate to checkout page"
