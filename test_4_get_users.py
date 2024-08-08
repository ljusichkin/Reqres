import pytest
import requests
import allure


@allure.feature('User Management')
@allure.suite('User Retrieval')
@allure.title('Get All Users List')
@allure.description('This test verifies that the list of all users can be retrieved successfully.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_all_users_list():
    response = requests.get('https://reqres.in/api/users?page=2')

    with allure.step('Verify response status code'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response is not empty'):
        assert len(response_data) > 0, 'Response JSON is empty'

    allure.attach(
        body=str(response.json()),
        name='Response JSON',
        attachment_type=allure.attachment_type.JSON
    )


@allure.feature('User Management')
@allure.suite('User Retrieval')
@allure.title('Get Single User')
@allure.description('This test verifies that the details of a single user can be retrieved successfully.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_single_user():
    response = requests.get('https://reqres.in/api/users/2')

    with allure.step('Verify response status code'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains "data"'):
        assert 'data' in response_data, 'Expected "data" key in response JSON'
        assert isinstance(response_data['data'], dict), 'Expected "data" to be a dictionary'

    user_data = response_data['data']

    with allure.step('Verify user data contains correct keys and values'):
        assert 'id' in user_data, 'User data does not contain "id" key'
        assert user_data['id'] == 2, f'Expected user ID 2, but got {user_data["id"]}'

    with allure.step('Verify user data contains "email" key and value'):
        assert 'email' in user_data, 'User data does not contain "email" key'
        assert user_data['email'] == 'janet.weaver@reqres.in', f'Expected email "janet.weaver@reqres.in", but got {user_data["email"]}'

    with allure.step('Verify user data contains "first_name" key and value'):
        assert 'first_name' in user_data, 'User data does not contain "first_name" key'
        assert user_data['first_name'] == 'Janet', f'Expected first name "Janet", but got {user_data["first_name"]}'

    with allure.step('Verify user data contains "last_name" key and value'):
        assert 'last_name' in user_data, 'User data does not contain "last_name" key'
        assert user_data['last_name'] == 'Weaver', f'Expected last name "Weaver", but got {user_data["last_name"]}'

    with allure.step('Verify user data contains "avatar" key and value'):
        assert 'avatar' in user_data, 'User data does not contain "avatar" key'
        assert user_data['avatar'] == 'https://reqres.in/img/faces/2-image.jpg', f'Expected avatar URL "https://reqres.in/img/faces/2-image.jpg", but got {user_data["avatar"]}'

    with allure.step('Verify response contains "support"'):
        assert 'support' in response_data, 'Expected "support" key in response JSON'
        assert isinstance(response_data['support'], dict), 'Expected "support" to be a dictionary'

    support_data = response_data['support']

    with allure.step('Verify support data contains "url" key and value'):
        assert 'url' in support_data, 'Support data does not contain "url" key'
        assert support_data['url'] == 'https://reqres.in/#support-heading', f'Expected support URL "https://reqres.in/#support-heading", but got {support_data["url"]}'

    with allure.step('Verify support data contains "text" key and value'):
        assert 'text' in support_data, 'Support data does not contain "text" key'
        assert support_data['text'] == 'To keep ReqRes free, contributions towards server costs are appreciated!', f'Expected support text "To keep ReqRes free, contributions towards server costs are appreciated!", but got {support_data["text"]}'

    allure.attach(
        body=str(response.json()),
        name='Response JSON',
        attachment_type=allure.attachment_type.JSON
    )


# Test for Getting a Non-Existent User (test_get_user_by_id)
@allure.feature('User Management')
@allure.suite('User Retrieval')
@allure.title('Get Non-Existent User by ID')
@allure.description('This test verifies that attempting to retrieve a non-existent user by ID returns a 404 error.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_a_non_existent_user_by_id():
    with allure.step('Send GET request to retrieve non-existent user'):
        response = requests.get('https://reqres.in/api/users/23')

    with allure.step('Verify response status code'):
        assert response.status_code == 404, f'Expected Status Code 404, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response is an empty JSON object'):
        assert response_data == {}, "Expected response body to be an empty JSON object {}"



