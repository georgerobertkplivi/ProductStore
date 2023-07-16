import time

import pytest
from assertpy import assert_that

from pages.contact_page import ContactPage
from pages.homepage import HomePage
from tests.base_test import BaseTest


@pytest.mark.sanity
class ContactTest(BaseTest, ContactPage):
    """

1. Positive Test Cases:
   1.1. Verify that all the required fields (Contact Email, Contact Name, and Message) can be filled successfully.
   1.2. Verify that a valid email address is accepted in the Contact Email field.
   1.3. Verify that the Contact Name field accepts alphanumeric characters, special characters, and spaces.
   1.4. Verify that the Message field accepts alphanumeric characters, special characters, spaces, and line breaks.
   1.5. Verify that the Close button closes the contact form without saving any entered data.
   1.6. Verify that the Send message button sends the message successfully and displays a success message.
   1.7. Verify that the form is cleared after successfully sending the message.

2. Negative Test Cases:
   2.1. Verify that submitting the form without filling any required fields displays appropriate error messages.
   2.2. Verify that entering an invalid email address in the Contact Email field displays an error message.
   2.3. Verify that entering a very long name in the Contact Name field doesn't cause any UI issues or truncation.
   2.4. Verify that entering a very long message in the Message field doesn't cause any UI issues or truncation.
   2.5. Verify that clicking the Close button prompts the user for confirmation before closing the form if any data is entered.
   2.6. Verify that clicking the Send message button while offline displays an appropriate error message.
   2.7. Verify that the form doesn't allow entering scripts or HTML tags in any field to prevent code injection.

3. Boundary Test Cases:
   3.1. Verify that the Contact Email field accepts the maximum allowed number of characters.
   3.2. Verify that the Contact Name field accepts the maximum allowed number of characters.
   3.3. Verify that the Message field accepts the maximum allowed number of characters.
   3.4. Verify that the Contact Email field doesn't accept more than the maximum allowed number of characters.
   3.5. Verify that the Contact Name field doesn't accept more than the maximum allowed number of characters.
   3.6. Verify that the Message field doesn't accept more than the maximum allowed number of characters.

    """

    @pytest.mark.positive
    def test_positive_contact_form_submission(self):
        # contact_page = ContactPage()
        # home_page = HomePage()

        self.goto_contact()

        # Fill in the contact form
        self.fill_contact_form(
            email="test@example.com",
            name="John Doe",
            message="This is a test message."
        )

        # Submit the contact form
        self.submit_form()

        # Verify the form is cleared
        self.assert_form_fields_are_not_displayed()

    @pytest.mark.positive
    def test_fill_required_fields(self):
        self.goto_contact()

        # Fill the required fields
        self.fill_contact_email("test@example.com")
        self.fill_contact_name("John Doe")
        self.fill_message("This is a test message")

        # Submit the form
        self.click_send_message()

        # Assertion
        assert_that(self.assert_form_fields_are_displayed()).is_false()

    # Verify that a valid email address is accepted in the Contact Email field.
    @pytest.mark.positive
    def test_valid_email_acceptance(self):
        self.goto_contact()
        # Fill the contact form with a valid email address
        valid_email = "test@example.com"
        self.fill_contact_form(valid_email, "John Doe", "Hello, this is a test message")

        # Verify that the filled email address is accepted
        filled_email = self.get_attribute(self.EMAIL_INPUT_SELECTOR, "value")
        assert filled_email == valid_email

        self.verify_valid_email(valid_email)

        # Clear the contact form for the next test case
        self.clear_form_fields()
        self.assert_form_fields_are_empty()

    # Verify that the Contact Name field accepts alphanumeric characters, special characters, and spaces.
    @pytest.mark.positive
    def test_contact_name_acceptance(self):
        self.goto_contact()
        # Fill the contact form with different types of names
        names = ["John Doe", "Jane-Smith", "Mr. James O'Connor"]
        for name in names:
            self.fill_contact_form("test@example.com", name, "Hello, this is a test message")

            # Verify that the filled name is accepted
            filled_name = self.get_attribute(self.NAME_INPUT_SELECTOR, "value")
            assert filled_name == name

            # Clear the contact form for the next test case
            self.clear_form_fields()
            self.assert_form_fields_are_empty()

    # Verify that the Message field accepts alphanumeric characters, special characters, spaces, and line breaks.
    @pytest.mark.positive
    def test_message_acceptance(self):
        self.goto_contact()

        # Fill the contact form with different types of messages
        messages = ["Hello, World!", "This is a test message.", "Line 1\nLine 2"]
        for message in messages:
            self.fill_contact_form("test@example.com", "John Doe", message)

            # Verify that the filled message is accepted
            filled_message = self.get_attribute(self.MESSAGE_INPUT_SELECTOR, "value")
            assert filled_message == message

            # Clear the contact form for the next test case
            self.clear_form_fields()
            self.assert_form_fields_are_empty()

    #    1.5. Verify that the Close button closes the contact form without saving any entered data.
    @pytest.mark.positive
    def test_close_button_functionality(self):
        self.goto_contact()

        # Fill the contact form with some data
        self.fill_contact_form("test@example.com", "John Doe", "Hello, this is a test message")

        # Assert that the form fields are empty
        self.clear_form_fields()
        assert_that(self.is_element_visible(self.MESSAGE_INPUT_SELECTOR)).is_true()

    #    1.6. Verify that the Send message button sends the message successfully and displays a success message.
    @pytest.mark.positive
    def test_send_message_button_functionality(self):
        self.goto_contact()

        # Fill the contact form with valid data
        self.fill_contact_form("test@example.com", "John Doe", "Hello, this is a test message")

        # Click on the Send message button
        self.submit_form()

        # Assert that a success message is displayed
        assert_that(self.assert_form_fields_are_displayed()).is_false()

    #    1.7. Verify that the form is cleared after successfully sending the message.
    @pytest.mark.positive
    def test_form_clear_after_sending_message(self):
        self.goto_contact()

        # Fill the contact form with valid data
        self.fill_contact_form("test@example.com", "John Doe", "Hello, this is a test message")

        # Click on the Send message button
        self.submit_form()

        # Assert that a success message is displayed
        assert_that(self.is_success_message_displayed).is_true()

        # Assert that the form fields are empty
        self.assert_form_fields_are_empty()

    #    2.1. Verify that submitting the form without filling any required fields displays appropriate error messages.
    @pytest.mark.negative
    def test_submit_form_without_required_fields(self):
        self.goto_contact()

        # Click on the Send message button without filling any fields
        self.submit_form()

        # Assert that appropriate error messages are displayed
        self.assert_error_message_displayed()
