from seleniumbase import BaseCase


class BaseTest(BaseCase):
    base_url = "https://www.demoblaze.com/index.html"

    def setUp(self):
        super().setUp()
        # <<< Run custom setUp() code for tests AFTER the super().setUp() >>>
        self.open(self.base_url)
        self.maximize_window()

    def tearDown(self):
        self.save_teardown_screenshot()  # If test fails, or if "--screenshot"
        super().tearDown()
