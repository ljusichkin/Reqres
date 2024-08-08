import pytest
import requests
import allure

my_user_id = 0


@allure.feature('User Management')
@allure.suite('Create User')
@allure.title('Create User and Get ID')
@allure.description('This test verifies that a user can be created successfully with valid data.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_create_user():
    body = {
        "name": "morpheus",
        "job": "leader"
    }

    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request to create a user'):
        response = requests.post(
            'https://reqres.in/api/users',
            json=body,
            headers=headers
        )

    allure.attach(
        body=str(response.json()),
        name='Response JSON',
        attachment_type=allure.attachment_type.JSON
    )

    with allure.step('Verify response status code'):
        assert response.status_code == 201, f'Expected Status Code 201, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains "name"'):
        assert 'name' in response_data,'Response JSON does not contain "name" key'
        assert response_data['name'] == body['name'], f'Expected name {body["name"]}, but got {response_data["name"]}'

    with allure.step('Verify response contains "job"'):
        assert 'job' in response_data, 'Response JSON does not contain "job" key'
        assert response_data['job'] == body['job'], f'Expected job {body["job"]}, but got {response_data["job"]}'

    with allure.step('Verify response contains "id" and "createdAt"'):
        assert 'id' in response_data, 'Response JSON does not contain "id" key'
        assert 'createdAt' in response_data, 'Response JSON does not contain "createdAt" key'


@allure.feature('User Management')
@allure.suite('Create New User')
@allure.title('Create New User and Get ID')
@allure.description('This test verifies that a new user can be created successfully with valid data.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_create_new_user():
    global my_user_id
    body = {
        "name": "ljusichkin",
        "job": "QA Automation"
    }

    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request to create a new user'):
        response = requests.post(
            'https://reqres.in/api/users',
            json=body,
            headers=headers
        )

    allure.attach(
        body=str(response.json()),
        name='Response JSON',
        attachment_type=allure.attachment_type.JSON
    )

    with allure.step('Verify response status code'):
        assert response.status_code == 201, f'Expected Status Code 201, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains "name"'):
        assert 'name' in response_data,'Response JSON does not contain "name" key'
        assert response_data['name'] == body['name'], f'Expected name {body["name"]}, but got {response_data["name"]}'

    with allure.step('Verify response contains "job"'):
        assert 'job' in response_data, 'Response JSON does not contain "job" key'
        assert response_data['job'] == body['job'], f'Expected job {body["job"]}, but got {response_data["job"]}'

    with allure.step('Verify response contains "id" and "createdAt"'):
        assert 'id' in response_data, 'Response JSON does not contain "id" key'
        assert 'createdAt' in response_data, 'Response JSON does not contain "createdAt" key'

    my_user_id = response_data['id']


