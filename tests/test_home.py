import pytest

from pages.homepage import HomePage


class HomePageTest(HomePage):

    @pytest.mark.mm
    def test_homepage_load(self):
        self.open("https://www.demoblaze.com/index.html")
        self.verify_home_loads()
