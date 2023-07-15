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

    def goto_about(self):
        self.click(self.about_us)

    def goto_cart(self):
        self.click(self.cart)

    def goto_login(self):
        self.click(self.log_in)

    def goto_sign_up(self):
        self.click(self.sign_up)

