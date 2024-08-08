import pytest
import requests
import allure

import test_3_create_user


@allure.feature('User Management')
@allure.suite('User Update')
@allure.title('Update User Successfully')
@allure.description('This test verifies that a user can be updated successfully with valid credentials.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_update_user():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }

    headers = {'Content-Type': 'application/json'}

    with allure.step('Send PUT request to update user'):
        response = requests.put(
            'https://reqres.in/api/users/2',
            json=body,
            headers=headers
        )

    with allure.step('Verify response status code'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains "name"'):
        assert 'name' in response_data, 'Response JSON does not contain "name" key'
        assert response_data['name'] == body['name'], f'Expected name {body["name"]}, but got {response_data["name"]}'

    with allure.step('Verify response contains "job"'):
        assert 'job' in response_data, 'Response JSON does not contain "job" key'
        assert response_data['job'] == body['job'], f'Expected job {body["job"]}, but got {response_data["job"]}'

    with allure.step('Verify response contains "updatedAt"'):
        assert 'updatedAt' in response_data, 'Expected the key "updatedAt" to be present in the response data.'


@allure.feature('User Management')
@allure.suite('User Update')
@allure.title('Update Created User Successfully')
@allure.description('This test verifies that a created user can be updated successfully with valid credentials.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_update_created_user():
    user_id = test_3_create_user.my_user_id
    body = {
        "name": "Lusine Avetisyan",
        "job": "QA Engineer"
    }

    headers = {'Content-Type': 'application/json'}

    with allure.step('Send PUT request to update user'):
        response = requests.put(
            f'https://reqres.in/api/users/{user_id}',
            json=body,
            headers=headers
        )

    with allure.step('Verify response status code'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains "name"'):
        assert 'name' in response_data, 'Response JSON does not contain "name" key'
        assert response_data['name'] == body['name'], f'Expected name {body["name"]}, but got {response_data["name"]}'

    with allure.step('Verify response contains "job"'):
        assert 'job' in response_data, 'Response JSON does not contain "job" key'
        assert response_data['job'] == body['job'], f'Expected job {body["job"]}, but got {response_data["job"]}'

    with allure.step('Verify response contains "updatedAt"'):
        assert 'updatedAt' in response_data, 'Expected the key "updatedAt" to be present in the response data.'

    allure.attach(
        body=str(response.json()),
        name='Response JSON',
        attachment_type=allure.attachment_type.JSON
    )


