import pytest
from assertpy import assert_that

from pages.sign_up_page import SignUpPage
from tests.base_test import BaseTest
from faker import Faker


class SignUpPageTest(BaseTest, SignUpPage):
    """

   test cases for the SignUpPage:

1. Positive Test Cases:
   1.1. Verify that a user can successfully sign up with valid credentials.
   1.2. Verify that the sign-up form can handle and accept valid usernames and passwords with alphanumeric characters, special characters, and spaces.
   1.3. Verify that the user is redirected to the correct dashboard or home page after successful sign-up.

2. Negative Test Cases:
   2.1. Verify that appropriate error messages are displayed when attempting to sign up with an existing username.
   2.2. Verify that the sign-up form prevents sign-up with an empty username field.
   2.3. Verify that the sign-up form prevents sign-up with an empty password field.
   2.4. Verify that the sign-up form prevents sign-up with both empty username and password fields.
   2.5. Verify that the sign-up form enforces a minimum password length and displays an error message when the password is too short.

3. Boundary Test Cases:
   3.1. Verify that the sign-up form can handle and accept the maximum allowed number of characters for the username and password fields.
   3.2. Verify that the sign-up form does not allow sign-up with the username and password fields exceeding the maximum allowed number of characters.

4. Security Test Cases:
   4.1. Verify that the sign-up form does not expose the entered password as plain text.
   4.2. Verify that the sign-up form is protected against SQL injection attacks.
   4.3. Verify that the sign-up form is protected against Cross-Site Scripting (XSS) attacks.

5. Sign-In Link Test Cases:
   5.1. Verify that the "Sign In" link is present on the sign-up page.
   5.2. Verify that clicking the "Sign In" link redirects the user to the correct sign-in page.

6. Close Button Test Cases:
   6.1. Verify that the close button on the sign-up modal works and closes the sign-up form without any data being saved.

7. Logout Test Cases:
   7.1. Verify that a newly signed-up user is automatically logged in and can access the dashboard or home page.
   7.2. Verify that the "Logout" button is present on the dashboard or home page after signing up.
   7.3. Verify that clicking the "Logout" button logs out the user and redirects them to the correct sign-in page.


    """

    def test_successful_sign_up(self):
        self.goto_sign_up()

        # Generate random valid username and password using Faker
        faker = Faker()
        valid_username = faker.user_name()
        valid_password = faker.password()

        # Fill in the sign-up form with valid credentials
        self.fill_sign_up_form(valid_username, valid_password)
        self.click_sign_up_button()

        # Assert that the user is redirected to the correct dashboard or home page
        assert_that(self.get_alert_text()).contains("Sign up successful.")
        # For example, you can assert the URL or the presence of certain elements on the dashboard page

    def test_valid_usernames_passwords(self):
        self.goto_sign_up()

        # List of valid usernames and passwords to test
        faker = Faker()
        valid_credentials = [
            {"username": faker.user_name(), "password": "password123"}
            # Add more valid combinations as needed
        ]

        for credentials in valid_credentials:
            # Fill in the sign-up form with valid credentials
            self.fill_sign_up_form(credentials["username"], credentials["password"])
            self.click_sign_up_button()
            alert = self.switch_to_alert()
            alert_text = alert.text
            # validate the alert text
            assert_that(alert_text).contains("Sign up successful.")
            alert.accept()

    def test_redirect_after_sign_up(self):
        self.goto_sign_up()

        # Generate random valid username and password using Faker
        faker = Faker()
        valid_username = faker.user_name()
        valid_password = faker.password()

        # Fill in the sign-up form with valid credentials
        self.fill_sign_up_form(valid_username, valid_password)
        self.click_sign_up_button()
