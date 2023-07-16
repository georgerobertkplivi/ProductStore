import pytest
from pages.homepage import HomePage
from tests.base_test import BaseTest


class HomePageTest(HomePage, BaseTest):

    # @pytest.mark.mm
    def test_homepage_load(self):
        self.verify_home_loads()
