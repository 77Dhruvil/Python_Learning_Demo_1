import pytest
import allure
import requests


@allure.title("Test Post Request - Savvy Wallet Project")
@allure.description("TC#1 - Verify the Login with Valid Credential")
@allure.tag("Functional")
@allure.label("owner", "Dhruvil Patel")
@allure.testcase("TC#1")
@pytest.mark.Functional
def test_post_Login_valid_cread():
    base_url = "https://savvy-valet.concettoprojects.com/savvy-valet-api/public/api"
    base_path = "/login"
    URL = base_url + base_path
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    form_data = {
    "email" : "ritik@yopmail.com",
    "password" : "Admin@123",
    "device_type" : "android"
    }

    response = requests.post(url=URL,headers=headers,data=form_data)
    assert response.status_code == 200
    responseData = response.json()

    if "email" in responseData:
        email = responseData["email"]
        assert email == "ritik@yopmail.com", f"Expected email to be 'ritik@yopmail.com', but got '{email}'"
    if "password" in responseData:
        password = responseData["password"]
        assert password == "Admin@123", f"Expected password to be 'Admin@123', but got '{password}'"
    if "device_type" in responseData:
        device_type = responseData["device_type"]
        assert device_type == "Android", f"Expected device_type to be 'Android', but got '{device_type}'"


@allure.title("Test Post Request - Savvy Wallet Project")
@allure.description("TC#2 - Verify the Login with Blank email and Blank Password")
@allure.tag("Functional")
@allure.label("owner", "Dhruvil Patel")
@allure.testcase("TC#2")
@pytest.mark.Functional
def test_post_Login_without_cread():
    base_url = "https://savvy-valet.concettoprojects.com/savvy-valet-api/public/api"
    base_path = "/login"
    URL = base_url + base_path
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    form_data = {
    "email" : "",
    "password" : "",
    "device_type" : "android"
    }

    responseData = requests.post(url=URL, headers=headers, data=form_data)
    assert responseData.status_code == 422
    response = responseData.json()

    if "email" in responseData:
        email = responseData["email"]
        assert email == "", f"Expected email to be '', but got '{'The email field is required'}'"
    if "password" in responseData:
        password = responseData["password"]
        assert password == "", f"Expected password to be '', but got '{'The password field is required'}'"
    if "device_type" in responseData:
        device_type = responseData["device_type"]
        assert device_type == "Android", f"Expected device_type to be 'Android', but got '{device_type}'"



@allure.title("Test Post Request - Savvy Wallet Project")
@allure.description("TC#3 - Verify the Login with Blank email and valid Password")
@allure.tag("Functional")
@allure.label("owner", "Dhruvil Patel")
@allure.testcase("TC#3")
@pytest.mark.Functional
def test_post_Login_with_Blank_email_valid_password():
    base_url = "https://savvy-valet.concettoprojects.com/savvy-valet-api/public/api"
    base_path = "/login"
    URL = base_url + base_path
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    form_data = {
    "email" : "",
    "password" : "Admin@123",
    "device_type" : "android"
    }

    responseData = requests.post(url=URL, headers=headers, data=form_data)
    assert responseData.status_code == 422
    response = responseData.json()

    if "email" in responseData:
        email = responseData["email"]
        assert email == "" , f"Expected email to be '', but got '{'The email field is required'}'"
    if "password" in responseData:
        password = responseData["password"]
        assert password == "Admin@123", f"Expected password to be 'Admin@123', but got '{password}'"
    if "device_type" in responseData:
        device_type = responseData["device_type"]
        assert device_type == "Android", f"Expected device_type to be 'Android', but got '{device_type}'"

@allure.title("Test Post Request - Savvy Wallet Project")
@allure.description("TC#4 - Verify the Login with Valid email and Blank Password")
@allure.tag("Functional")
@allure.label("owner", "Dhruvil Patel")
@allure.testcase("TC#4")
@pytest.mark.Functional
def test_post_Login_with_valid_Email_Blank_Password():
    base_url = "https://savvy-valet.concettoprojects.com/savvy-valet-api/public/api"
    base_path = "/login"
    URL = base_url + base_path
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    form_data = {
    "email" : "ritik@yopmail.com",
    "password" : "",
    "device_type" : "android"
    }

    responseData = requests.post(url=URL, headers=headers, data=form_data)
    assert responseData.status_code == 422
    response = responseData.json()

    if "email" in responseData:
        email = responseData["email"]
        assert email == "ritik@yopmail.com", f"Expected email to be 'ritik@yopmail.com', but got '{email}'"

    if "password" in responseData:
        password = responseData["password"]
        assert password == "", f"Expected password to be '', but got '{'The password field is required'}'"

    if "device_type" in responseData:
        device_type = responseData["device_type"]
        assert device_type == "Android", f"Expected device_type to be 'Android', but got '{device_type}'"

@allure.title("Test Post Request - Savvy Wallet Project")
@allure.description("TC#5 - Verify the Login with Invalid email and Invalid Password")
@allure.tag("Functional")
@allure.label("owner", "Dhruvil Patel")
@allure.testcase("TC#5")
@pytest.mark.Functional
def test_post_Login_with_Invalid_Email_Invaild_Password():
    base_url = "https://savvy-valet.concettoprojects.com/savvy-valet-api/public/api"
    base_path = "/login"
    URL = base_url + base_path
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    form_data = {
    "email" : "ritik1@yopmail.com",
    "password" : "Test@1234",
    "device_type" : "android"
    }

    responseData = requests.post(url=URL, headers=headers, data=form_data)
    assert responseData.status_code == 422
    responseData = responseData.json()

    if "email" in responseData:
        email = responseData["email"]
        assert email == "ritik1@yopmail.com" , f"Expected email to be 'ritik@yopmail.com', but got '{'User not found'}'"

    if "password" in responseData:
        password = responseData["password"]
        assert password == "Test@1234", f"Expected password to be 'Admin@123', but got '{'User not Found'}'"

    if "device_type" in responseData:
        device_type = responseData["device_type"]
        assert device_type == "Android", f"Expected device_type to be 'Android', but got '{device_type}'"
@allure.title("Test Post Request - Savvy Wallet Project")
@allure.description("TC#6 - Verify the Login with valid email and Invalid Password")
@allure.tag("Functional")
@allure.label("owner", "Dhruvil Patel")
@allure.testcase("TC#6")
@pytest.mark.Functional
def test_post_Login_with_valid_email_Invalid_password():
    base_url = "https://savvy-valet.concettoprojects.com/savvy-valet-api/public/api"
    base_path = "/login"
    URL = base_url + base_path
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    form_data = {
    "email" : "ritik@yopmail.com",
    "password" : "Test@123",
    "device_type" : "android"
    }

    responseData = requests.post(url=URL, headers=headers, data=form_data)
    assert responseData.status_code == 422
    responseData = responseData.json()

    if "email" in responseData:
        email = responseData["email"]
        assert email == "ritik@yopmail.com" , f"Expected email to be 'ritik@yopmail.com' , but got '{email}'"

    if "password" in responseData:
        password = responseData["password"]
        assert password == "Test@123" , f"Expected password to be 'Admin@123' , but got '{'Invalid Email or password'}'"

    if "device_type" in responseData:
        device_type = responseData["device_type"]
        assert device_type == "Android", f"Expected device_type to be 'Android', but got '{device_type}'"

@allure.title("Test Post Request - Savvy Wallet Project")
@allure.description("TC#7 - Verify with the capital Valid Email and password")
@allure.tag("Functional")
@allure.label("owner", "Dhruvil Patel")
@allure.testcase("TC#7")
@pytest.mark.Functional
def test_post_Login_with_capital_valid_email_valid_password():
    base_url = "https://savvy-valet.concettoprojects.com/savvy-valet-api/public/api"
    base_path = "/login"
    URL = base_url + base_path
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    form_data = {
    "email" : "RITIK@YOPMAIL.COM",
    "password" : "ADMIN@123",
    "device_type" : "android"
    }

    responseData = requests.post(url=URL, headers=headers, data=form_data)
    assert responseData.status_code == 422
    responseData = responseData.json()

    if "email" in responseData:
        email = responseData["email"]
        assert email == "RITIK@YOPMAIL.COM", f"Expected email to be 'ritik@yopmail.com', but got '{email}'"

    if "password" in responseData:
        password = responseData["password"]
        assert password == "ADMIN@123", f"Expected password to be 'Admin@123', but got '{'Incorrect email or password'}'"

    if "device_type" in responseData:
        device_type = responseData["device_type"]
        assert device_type == "Android", f"Expected device_type to be 'Android', but got '{device_type}'"


@allure.title("Test Post Request - Savvy Wallet Project")
@allure.description("TC#8 - Verify the Login with Invalid format of email and valid Password")
@allure.tag("Functional")
@allure.label("owner", "Dhruvil Patel")
@allure.testcase("TC#8")
@pytest.mark.Functional
def test_post_Login_with_valid_email_valid_password():
    base_url = "https://savvy-valet.concettoprojects.com/savvy-valet-api/public/api"
    base_path = "/login"
    URL = base_url + base_path
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    form_data = {
    "email" : "sdiofjdijfodsifjodij@osidjsofjd",
    "password" : "Admin@123",
    "device_type" : "android"
    }

    responseData = requests.post(url=URL, headers=headers, data=form_data)
    assert responseData.status_code == 422
    responseData = responseData.json()

    if "email" in responseData:
        email = responseData["email"]
        assert email == "dkjwoewjrieojr@ffsidfsodifdsf", f"Expected email to be 'ritik@yopmail.com', but got '{'The email field format is invalid'}'"

    if "password" in responseData:
        password = responseData["password"]
        assert password == "Admin@123", f"Expected password to be 'Admin@123', but got '{password}'"

    if "device_type" in responseData:
        device_type = responseData["device_type"]
        assert device_type == "Android", f"Expected device_type to be 'Android', but got '{device_type}'"

