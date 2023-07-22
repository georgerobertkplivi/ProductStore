from pages.homepage import HomePage


class SignUpPage(HomePage):
    signUpUserName = "#sign-username"
    signUpPassword = "#sign-password"
    signUpCloseButton = "div[id='logInModal'] div[class='modal-footer'] button:nth-child(1)"
    signUpButton = "button[onclick='register()']"
    signInHeader = "#signInModalLabel"
    signIn = "#signin2"

    def enter_sign_up_username(self, username):
        self.update_text(self.signUpUserName, username)

    def enter_sign_up_password(self, password):
        self.update_text(self.signUpPassword, password)

    def click_sign_up_close_button(self):
        self.click(self.signUpCloseButton)

    def click_sign_up_button(self):
        self.click(self.signUpButton)

    def get_sign_in_header_text(self):
        return self.get_text(self.signInHeader)

    def click_sign_in_link(self):
        self.click(self.signIn)

    def fill_sign_up_form(self, username, password):
        self.enter_sign_up_username(username)
        self.enter_sign_up_password(password)

    def sign_up_user(self, valid_username, valid_password):
        # Fill in the sign-up form with valid credentials
        self.fill_sign_up_form(valid_username, valid_password)
        self.click_sign_up_button()
