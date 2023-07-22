from pages.homepage import HomePage


class LoginPage(HomePage):
    user_name = "#loginusername"
    password = "#loginpassword"
    close_button = "div[id='logInModal'] div[class='modal-footer'] button:nth-child(1)"
    login_button = "button[onclick='logIn()']"
    user_email_locator = "#nameofuser"
    logout_button_locator = "#logout2"

    def verify_login_page_loads(self):
        self.assert_element_present(self.user_name)
        self.assert_element_present(self.password)
        self.assert_element_present(self.close_button)
        self.assert_element_present(self.login_button)

    def enter_user_name(self, username):
        self.update_text(self.user_name, username)

    def enter_password(self, password):
        self.update_text(self.password, password)

    def click_close_button(self):
        self.click(self.close_button)

    def click_login_button(self):
        self.click(self.login_button)

    def fill_login_form(self, username, password):
        self.verify_login_page_loads()
        self.enter_user_name(username)
        self.enter_password(password)

    def get_username(self):
        return self.get_text(self.user_email_locator)

    def assert_logout_button_present(self):
        self.assert_element_present(self.logout_button_locator)
