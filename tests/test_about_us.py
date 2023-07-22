import pytest
from assertpy import assert_that

from pages.about_us_page import AboutUsPage
from tests.base_test import BaseTest


class TestAboutUsPage(BaseTest, AboutUsPage):
    @pytest.mark.about
    def test_about_us_page_loads(self):
        self.goto_about()
        assert_that(self.get_about_us_heading_text()).contains("About us")

    @pytest.mark.about
    def test_play_button_plays_video(self):
        self.goto_about()
        self.click_play_video_button()
        self.wait(5)
        # assertions to verify that the video is playing
        self.assert_element_present(self.pause_button_locator)

    @pytest.mark.about
    def test_close_button_closes_about_us_page(self):
        self.goto_about()
        self.click_close_button()
        self.assert_element_not_present(self.about_us_heading)
