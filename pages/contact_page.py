from assertpy import assert_that

from pages.homepage import HomePage


class ContactPage(HomePage):
    # Locators
    FORM_TITLE_SELECTOR = "#exampleModalLabel"
    EMAIL_INPUT_SELECTOR = "#recipient-email"
    NAME_INPUT_SELECTOR = "#recipient-name"
    MESSAGE_INPUT_SELECTOR = "#message-text"
    CLOSE_BUTTON_SELECTOR = "//div[@id='exampleModal']//button[@type='button'][normalize-space()='Close']"
    SEND_BUTTON_SELECTOR = "button[onclick='send()']"
    SUCCESS_MESSAGE_SELECTOR = "div#success_message"

    def fill_contact_form(self, email, name, message):
        self.update_text(self.EMAIL_INPUT_SELECTOR, email)
        self.update_text(self.NAME_INPUT_SELECTOR, name)
        self.update_text(self.MESSAGE_INPUT_SELECTOR, message)

    def submit_form(self):
        self.click(self.SEND_BUTTON_SELECTOR)

    def close_form(self):
        self.click(self.CLOSE_BUTTON_SELECTOR)

    def get_email(self):
        return self.get_attribute(self.EMAIL_INPUT_SELECTOR, "value")

    def get_name(self):
        return self.get_attribute(self.NAME_INPUT_SELECTOR, "value")

    def get_message(self):
        return self.get_attribute(self.MESSAGE_INPUT_SELECTOR, "value")

    def fill_contact_email(self, email):
        self.update_text(self.EMAIL_INPUT_SELECTOR, email)

    def fill_contact_name(self, name):
        self.update_text(self.NAME_INPUT_SELECTOR, name)

    def fill_message(self, message):
        self.update_text(self.MESSAGE_INPUT_SELECTOR, message)

    def click_send_message(self):
        self.click(self.SEND_BUTTON_SELECTOR)

    def is_success_message_displayed(self):
        self.is_element_present(self.SEND_BUTTON_SELECTOR)
        self.is_element_present(self.NAME_INPUT_SELECTOR)
        self.is_element_present(self.MESSAGE_INPUT_SELECTOR)
        self.is_element_present(self.EMAIL_INPUT_SELECTOR)

    def clear_form_fields(self):
        self.clear(self.NAME_INPUT_SELECTOR)
        self.clear(self.MESSAGE_INPUT_SELECTOR)
        self.clear(self.EMAIL_INPUT_SELECTOR)

    def verify_valid_email(self, email):
        return assert_that(email).contains("@")

    def assert_form_fields_are_empty(self):
        assert_that(self.get_attribute(self.EMAIL_INPUT_SELECTOR, "value")).is_empty()
        assert_that(self.get_attribute(self.NAME_INPUT_SELECTOR, "value")).is_empty()
        assert_that(self.get_attribute(self.MESSAGE_INPUT_SELECTOR, "value")).is_empty()

    def assert_success_message_displayed(self):
        success_message = "css:#success_message"
        assert_that(self.is_element_visible(success_message)).is_true()

    def assert_error_message_displayed(self):
        error_message = "css:#error_message"
        assert_that(self.is_element_visible(error_message)).is_false()

    def assert_form_fields_are_not_displayed(self):
        assert_that(self.is_element_visible(self.SEND_BUTTON_SELECTOR)).is_false()
        assert_that(self.is_element_visible(self.NAME_INPUT_SELECTOR)).is_false()
        assert_that(self.is_element_visible(self.MESSAGE_INPUT_SELECTOR)).is_false()
        assert_that(self.is_element_visible(self.EMAIL_INPUT_SELECTOR)).is_false()

    def assert_form_fields_are_displayed(self):
        assert_that(self.is_element_visible(self.SEND_BUTTON_SELECTOR)).is_false()
        assert_that(self.is_element_visible(self.NAME_INPUT_SELECTOR)).is_false()
        assert_that(self.is_element_visible(self.MESSAGE_INPUT_SELECTOR)).is_false()
        assert_that(self.is_element_visible(self.EMAIL_INPUT_SELECTOR)).is_false()
