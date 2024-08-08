import pytest
import requests
import allure
import time


@allure.feature('User Management')
@allure.suite('Response Timing')
@allure.title('Handle Delayed Response')
@allure.description('This test verifies that the API can handle a delayed response correctly.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_delayed_response():
    headers = {'Content-Type': 'application/json'}
    start_time = time.time()

    with allure.step('Send GET request with delay'):
        response = requests.get(
            'https://reqres.in/api/users?delay=3',
            headers=headers
        )
    end_time = time.time()
    elapsed_time = end_time - start_time

    with allure.step('Verify response status code'):
        assert response.status_code == 200, f'Expected status code 204, but got {response.status_code}'

    with allure.step('Verify response time is at least 3 seconds'):
        assert elapsed_time >= 3, f'Expected elapsed time to be at least 3 seconds, but got {elapsed_time}'

    allure.attach(
        body=str(response.json()),
        name='Response JSON',
        attachment_type=allure.attachment_type.JSON
    )
