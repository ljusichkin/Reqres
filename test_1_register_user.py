import pytest
import requests
import allure

my_id = None
my_token = None


@allure.feature('User Management')
@allure.suite('User Registration')
@allure.title('Register User')
@allure.description('This test verifies that a new user can be registered successfully with valid credentials.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_register_user():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request to register user'):
        response = requests.post(
            'https://reqres.in/api/register',
            json=body,
            headers=headers
        )

    allure.attach(
        body=str(response.json()),
        name='Response JSON',
        attachment_type=allure.attachment_type.JSON
    )

    with allure.step('Verify response status code'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains "id"'):
        assert 'id' in response_data, 'Response JSON does not contain "id" key'

    with allure.step('Verify "id" is not empty'):
        assert response_data['id'], 'Expected "id" to be non-empty'

    with allure.step('Verify response contains "token"'):
        assert 'token' in response_data, 'Response JSON does not contain "token" key'

    with allure.step('Verify "token" is not empty'):
        assert response_data['token'], 'Expected "token" to be non-empty'

    global my_id
    global my_token

    my_id = response_data.get('id')
    my_token = response_data.get('token')


@allure.feature('User Management')
@allure.suite('User Registration')
@allure.title('Negative Register User Missing Password')
@allure.description('This test verifies that the registration fails when the password is missing.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_negative_register_user_missing_password():
    body = {
        "email": "sydney@fife"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request without password'):
        response = requests.post(
            'https://reqres.in/api/register',
            json=body,
            headers=headers
        )

    with allure.step('Verify the response status code is 400'):
        assert response.status_code == 400, f'Expected Status Code 400, but got {response.status_code}'

    allure.attach(
        body=str(response.json()),
        name='Response JSON',
        attachment_type=allure.attachment_type.JSON
    )

    response_data = response.json()

    with allure.step('Verify the response contains error message'):
        assert 'error' in response_data, 'Expected "error" key in response JSON'

    with allure.step('Verify the error message is "Missing password"'):
        assert response_data['error'] == 'Missing password', f'Expected error message "Missing password", but got {response_data["error"]}'


@allure.feature('User Management')
@allure.suite('User Registration')
@allure.title('Negative Register User Missing Email')
@allure.description('This test verifies that the registration fails when the email is missing.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_negative_register_user_missing_email():
    body = {
        "password": "pistol"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request without email'):
        response = requests.post(
            'https://reqres.in/api/register',
            json=body,
            headers=headers
        )

    with allure.step('Verify the response status code is 400'):
        assert response.status_code == 400, f'Expected Status Code 400, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify the response contains error message'):
        assert 'error' in response_data, 'Expected error message in response'

    with allure.step('Verify the error message is "Missing email or username"'):
        assert response_data['error'] == 'Missing email or username', f'Expected error message "Missing email or username", but got {response_data["error"]}'


@allure.feature('User Management')
@allure.suite('User Registration')
@allure.title('Negative Register User Invalid Email')
@allure.description('This test verifies that the registration fails when an invalid email is provided.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_negative_register_user_invalid_email():
    body = {
        "email": "not-an-email",
        "password": "pistol"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request with invalid email'):
        response = requests.post(
            'https://reqres.in/api/register',
            json=body,
            headers=headers
        )

    with allure.step('Verify the response status code is 400'):
        assert response.status_code == 400, f'Expected Status Code 400, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify the response contains error message'):
        assert 'error' in response_data, 'Expected error message in response'
        assert response_data['error'] == 'Note: Only defined users succeed registration', f'Unexpected error message: {response_data["error"]}'
