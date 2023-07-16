import time

import pytest
from pages.homepage import HomePage
from tests.base_test import BaseTest


@pytest.mark.home
@pytest.mark.sanity
class HomePageTest(HomePage, BaseTest):

    def test_homepage_load(self):
        self.verify_home_loads()

    def test_filter_by_phone(self):
        self.click_on_phones_category()
        self.scroll_to_element(self.LAST_CARD)
        self.get_all_items()
        self.verify_number_all_phone()

    def test_filter_by_laptops(self):
        self.click_on_laptops_category()
        self.scroll_to_element(self.PREV_BUTTON)
        self.get_all_items()
        self.verify_all_laptops()

    def test_filter_by_monitors(self):
        self.click_on_monitors_category()
        self.scroll_to_element(self.PREV_BUTTON)
        self.get_all_items()
        self.verify_all_monitors()

    def test_goto_next_page(self):
        self.verify_home_loads()
        self.scroll_to_element(self.NEXT_BUTTON)
        self.goto_next_page()
        self.verify_next_page()
