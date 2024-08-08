import pytest
import requests
import allure

import test_3_create_user


@allure.feature('User Management')
@allure.suite('User Partial Update')
@allure.title('Partial Update User Successfully')
@allure.description('This test verifies that a user can be partially updated with valid data.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_partial_update_user():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send PATCH request to update user'):
        response = requests.patch(
            'https://reqres.in/api/users/2',
            json=body,
            headers=headers
        )

    with allure.step('Verify response status code'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains "name" key and value'):
        assert 'name' in response_data, 'Response JSON does not contain "name" key'
        assert response_data['name'] == body['name'], f'Expected name {body["name"]}, but got {response_data["name"]}'

    with allure.step('Verify response contains "job" key and value'):
        assert 'job' in response_data, 'Response JSON does not contain "job" key'
        assert response_data['job'] == body['job'], f'Expected job {body["job"]}, but got {response_data["job"]}'

    with allure.step('Verify response contains "updatedAt" key'):
        assert 'updatedAt' in response_data, 'Expected the key "updatedAt" to be present in the response data.'


@allure.feature('User Management')
@allure.suite('Created User Partial Update')
@allure.title('Partial Update Created User Successfully')
@allure.description('This test verifies that a created user can be partially updated with valid data.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_partial_update_created_user():
    user_id = test_3_create_user.my_user_id
    body = {
        "name": "Lusine Avetisyan",
        "job": "QA Engineer Lead"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send PATCH request to update created user'):
        response = requests.patch(
            f'https://reqres.in/api/users/{user_id}',
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

    with allure.step('Verify response contains "name" key and value'):
        assert 'name' in response_data, 'Response JSON does not contain "name" key'
        assert response_data['name'] == body['name'], f'Expected name {body["name"]}, but got {response_data["name"]}'

    with allure.step('Verify response contains "job" key and value'):
        assert 'job' in response_data, 'Response JSON does not contain "job" key'

    with allure.step('Verify response contains "updatedAt" key'):
        assert 'updatedAt' in response_data, 'Expected the key "updatedAt" to be present in the response data.'


