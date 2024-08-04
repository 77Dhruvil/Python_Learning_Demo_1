import json
import pytest
import allure
import requests
@allure.title("Test Post Request - Fovero Project")
@allure.description("TC#1 - Verify the data with valid Credential")
@allure.tag("Functional")
@allure.label("owner", "Dhruvil Patel")
@allure.testcase("TC#1")
@pytest.mark.Functional
def test_post_Login_api():
    base_url = "https://fovero-staging.concettoprojects.com/fovero-organization-api/public/api"
    base_path = "/login"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
    "email": "tejas@yopmail.com",
    "password": "Test@123"
}

    responseData = requests.post(URL,  payload , headers)
    print(responseData)
    assert responseData.status_code == 200
    response = responseData.json()
    print(response)

    if "email" in responseData:
        email = responseData['email']
        assert email == "tejas@yopmail.com", f"Expected email to be 'tejas@yopmail.com', but got {email}'"

    if "password" in responseData:
        password = responseData['password']
        assert password == "Test@123", f"Expected email to be 'Test@123', but got {password}'"

@allure.title("Test Post Request - Fovero Project")
@allure.description("TC#2 - Verify the data with Invalid Credential")
@allure.tag("Functional")
@allure.label("owner", "Dhruvil Patel")
@allure.testcase("TC#2")
@pytest.mark.Functional
def test_post_Login_api_Invalid_cred():
    base_url = "https://fovero-staging.concettoprojects.com/fovero-organization-api/public/api"
    base_path = "/login"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
    "email": "tejas1@yopmail.com",
    "password": "Test@1233"
}

    responseData = requests.post(URL,  payload , headers)
    print(responseData)
    assert responseData.status_code == 422
    response = responseData.json()
    print(response)

    if "email" in responseData:
        email = responseData['email']
        assert email == "tejas1@yopmail.com", f"Expected email to be 'tejas@yopmail.com', but got {email}'"

    if "password" in responseData:
        password = responseData['password']
        assert password == "Test@1233", f"Expected email to be 'Test@123', but got {password}'"


@allure.title("Test Post Request - Fovero Project")
@allure.description("TC#3 - Verify the data with Blank Email and Blank Password")
@allure.tag("Functional")
@allure.label("owner", "Dhruvil Patel")
@allure.testcase("TC#3")
@pytest.mark.Functional
def test_post_Login_api_Blank_Email_Blank_Password():
        base_url = "https://fovero-staging.concettoprojects.com/fovero-organization-api/public/api"
        base_path = "/login"
        URL = base_url + base_path
        headers = {"Content-Type": "application/json"}
        payload = {
            "email": "",
            "password": ""
        }

        responseData = requests.post(URL, payload, headers)
        print(responseData)
        assert responseData.status_code == 422
        response = responseData.json()
        print(response)

        if "email" in responseData:
            email = responseData['email']
            assert email == "", f"Expected email to be 'tejas@yopmail.com', but got {''}'"

        if "password" in responseData:
            password = responseData['password']
            assert password == "", f"Expected email to be 'Test@123', but got {password}'"

