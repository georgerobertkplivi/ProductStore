import pytest

from pages.login_page import LoginPage
from tests.base_test import BaseTest
from faker import Faker
from assertpy import assert_that


class LoginPageTest(BaseTest, LoginPage):
    """

Login Page:

1. Positive Test Cases:
   1.1. Verify that a user can successfully log in with valid credentials.
   1.2. Verify that the login form can handle and accept valid usernames and passwords with alphanumeric characters, special characters, and spaces.
   1.3. Verify that the user is redirected to the correct dashboard or home page after successful login.

2. Negative Test Cases:
   2.1. Verify that appropriate error messages are displayed when attempting to log in with an invalid or non-existing username.
   2.2. Verify that appropriate error messages are displayed when attempting to log in with an incorrect password for a valid username.
   2.3. Verify that the login form prevents login with an empty username field.
   2.4. Verify that the login form prevents login with an empty password field.
   2.5. Verify that the login form prevents login with both empty username and password fields.

3. Boundary Test Cases:
   3.1. Verify that the login form can handle and accept the maximum allowed number of characters for the username and password fields.
   3.2. Verify that the login form does not allow login with the username and password fields exceeding the maximum allowed number of characters.
   3.3. Verify that the login form can handle and accept the minimum allowed number of characters for the username and password fields.
   3.4. Verify that the login form does not allow login with the username and password fields below the minimum allowed number of characters.

4. Security Test Cases:
   4.1. Verify that the login form does not expose the entered password as plain text.
   4.2. Verify that the login form is protected against SQL injection attacks.
   4.3. Verify that the login form is protected against Cross-Site Scripting (XSS) attacks.

5. Logout Test Cases:
   5.1. Verify that a logged-in user can successfully log out from the system.
   5.2. Verify that after logging out, the user is redirected to the login page or a designated logout page.

6. Remember Me Test Cases:
   6.1. Verify that the "Remember Me" functionality works as expected, allowing the user to stay logged in even after closing and reopening the browser.


    """

    @pytest.mark.login
    def test_successful_login(self):
        self.goto_login()

        # Replace 'valid_username' and 'valid_password' with actual valid credentials
        faker = Faker()
        valid_username = faker.user_name()  # Generate a random username
        valid_password = faker.password()  # Generate a random password

        # Fill in the login form with valid credentials
        self.fill_login_form(valid_username, valid_password)

        # Click the login button
        self.click_login_button()
        self.accept_alert()

        # Assert that the user is redirected to the correct dashboard or home page
        # Add your assertions here based on the behavior of your application after successful login
        assert_that(self.get_username()).contains(valid_username)
        assert_that(self.is_element_present(self.logout_button_locator)).is_true()
        self.assert_logout_button_present()
        # For example, you can assert the URL or the presence of certain elements on the dashboard page