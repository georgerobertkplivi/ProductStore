from seleniumbase import BaseCase
from assertpy import assert_that


class HomePage(BaseCase):
    logo = "#nava"
    home = "//a[.='Home (current)']"
    cart = "//a[@id='cartur']"
    about_us = "//a[.='About us']"
    contact_us = "//a[.='Contact']"
    log_in = "//a[.='Log in']"
    sign_up = "//a[.='Sign up']"
    carousel_next = ".carousel-control-next-icon"
    carousel_prev = ".carousel-control-prev-icon"
    item_price_lable = "//h5[contains(.,'$')]"
    PREV_BUTTON = "#prev2"
    NEXT_BUTTON = "#next2"
    LAST_CARD = "img[src='imgs/HTC_M9.jpg']"

    def verify_home_loads(self):
        assert_that(self.get_text(self.logo)).contains("PRODUCT STORE")
        assert_that(self.get_text(self.home)).contains("Home")
        assert_that(self.get_text(self.contact_us)).contains("Contact")
        assert_that(self.get_text(self.about_us)).contains("About us")
        assert_that(self.get_text(self.cart)).contains("Cart")
        assert_that(self.get_text(self.log_in)).contains("Log in")
        assert_that(self.get_text(self.sign_up)).contains("Sign up")

    def next_carousel(self):
        self.click(self.carousel_next)

    def prev_carousel(self):
        self.click(self.carousel_prev)

    def goto_home(self):
        self.click(self.home)
        self.verify_home_loads()

    def goto_contact(self):
        self.click(self.contact_us)
        self.verify_home_loads()

    def goto_about(self):
        self.click(self.about_us)

    def goto_cart(self):
        self.click(self.cart)

    def goto_login(self):
        self.click(self.log_in)

    def goto_sign_up(self):
        self.click(self.sign_up)

    def click_on_phones_category(self):
        self.click("//a[contains(.,'Phones')]")

    def get_all_items(self):
        return len(self.get_text(self.item_price_lable))

    def verify_number_all_phone(self):
        assert_that(self.get_all_items()).is_equal_to(4)

    def click_on_laptops_category(self):
        self.click("//a[contains(.,'Laptops')]")

    def verify_all_laptops(self):
        assert_that(self.get_all_items()).is_equal_to(4)

    def click_on_monitors_category(self):
        self.click("//a[contains(.,'Monitors')]")

    def verify_all_monitors(self):
        assert_that(self.get_all_items()).is_equal_to(4)

    def goto_next_page(self):
        self.scroll_to_element(self.NEXT_BUTTON)
        self.click(self.NEXT_BUTTON)

    def get_macbook(self):
        return self.get_text("//a[normalize-space()='MacBook Pro']")

    def verify_next_page(self):
        # self.scroll_to_element(self.PREV_BUTTON)
        assert_that(self.is_element_visible(self.PREV_BUTTON)).is_true()
        # assert_that(self.get_macbook()).contains("MacBook Pro")

    def get_alert_text(self):
        alert = self.switch_to_alert()
        return alert.text



