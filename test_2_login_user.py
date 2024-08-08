import pytest
import requests
import allure


@allure.feature('User Management')
@allure.suite('User Authentication')
@allure.title('Successful Login')
@allure.description('This test verifies that a user can log in successfully with valid credentials.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_login_user():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request to login with valid credentials'):
        response = requests.post(
            'https://reqres.in/api/login',
            json=body,
            headers=headers
        )

    with allure.step('Verify response status code'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains "token"'):
        assert 'token' in response_data, 'Response JSON does not contain "token" key'

    with allure.step('Verify "token" is not empty'):
        assert response_data['token'] != "", 'Expected "token" to be non-empty'


@allure.feature('User Management')
@allure.suite('User Authentication')
@allure.title('Negative Login User Missing Password')
@allure.description('This test verifies that login fails when the password is missing.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_negative_login_user_missing_password():
    body = {
        "email": "peter@klaven"
    }

    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request to login without password'):
        response = requests.post(
            'https://reqres.in/api/login',
            json=body,
            headers=headers
        )

    with allure.step('Verify response status code'):
        assert response.status_code == 400, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    allure.attach(
        body=str(response_data),
        name='Response JSON',
        attachment_type=allure.attachment_type.JSON
    )

    with allure.step('Verify the response contains error message'):
        assert 'error' in response_data, 'Expected error message in response'

    with allure.step('Verify the error message'):
        assert response_data['error'] == 'Missing password', f'Unexpected error message: {response_data["error"]}'
