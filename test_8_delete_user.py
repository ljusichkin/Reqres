import pytest
import requests
import allure


@allure.feature('User Management')
@allure.suite('User Deletion')
@allure.title('Delete User')
@allure.description('This test verifies that a user can be successfully deleted.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_delete_user():
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send DELETE request to delete user'):
        response = requests.delete(
            'https://reqres.in/api/users/2',
            headers=headers)

    with allure.step('Verify response status code'):
        assert response.status_code == 204, f'Expected status code 204, but got {response.status_code}'
