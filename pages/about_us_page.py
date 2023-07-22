from seleniumbase import BaseCase

from pages.homepage import HomePage


class AboutUsPage(HomePage):
    play_video_button = "button[title='Play Video'] span[class='vjs-icon-placeholder']"
    about_us_heading = "#videoModalLabel"
    close_button = "div[id='videoModal'] div[class='modal-footer'] button[type='button']"
    video_time_locator = ".vjs-remaining-time-display"
    pause_button_locator = "button[title='Pause'] span[class='vjs-icon-placeholder']"

    def click_play_video_button(self):
        self.js_click(self.play_video_button)

    def get_about_us_heading_text(self):
        return self.get_text(self.about_us_heading)

    def click_close_button(self):
        self.click(self.close_button)

    def get_video_time(self):
        return self.get_text(self.video_time_locator)
