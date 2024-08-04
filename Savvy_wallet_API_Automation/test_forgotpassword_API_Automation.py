import pytest
import allure
import requests
@allure.title("Test Post Request - Savvy Wallet Project")
@allure.description("TC#1 - Verify the Forgot Password with Blank email")
@allure.tag("Functional")
@allure.label("owner", "Dhruvil Patel")
@allure.testcase("TC#1")
@pytest.mark.Functional

def test_post_forgot_password_blank_email():
    base_url = "https://savvy-valet.concettoprojects.com/savvy-valet-api/public/api"
    base_path = "/forgot-password"
    URL = base_url + base_path
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    form_data = {

        "email": ""
    }

    responseData = requests.post(URL, data=form_data, headers=headers)
    assert responseData.status_code == 422
    response = responseData.json()

    if "email" in responseData:
        email = responseData["email"]
        assert email == "" , f"Expected email to be 'dhruvil.patel+9999@concettolabs.com', but got '{'The email field is required'}'"


@allure.title("Test Post Request - Savvy Wallet Project")
@allure.description("TC#2 - Verify the Forgot Password with Invalid email")
@allure.tag("Functional")
@allure.label("owner", "Dhruvil Patel")
@allure.testcase("TC#2")
@pytest.mark.Functional

def test_post_forgot_password_Invalid_email():
    base_url = "https://savvy-valet.concettoprojects.com/savvy-valet-api/public/api"
    base_path = "/forgot-password"
    URL = base_url + base_path
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    form_data = {

        "email": "dhruvil+000@concettolabs.com"
    }
    responseData = requests.post(URL, data=form_data, headers=headers)
    assert responseData.status_code == 422
    response = responseData.json()

    if "email" in responseData:
        email = responseData['email']
        assert email == "dhruvil+000@concettolabs.com" , f"Expected email to be 'dhruvil.patel+9999@concettolabs.com', but got {'Email not found'}'"

@allure.title("Test Post Request - Savvy Wallet Project")
@allure.description("TC#3 - Verify the Forgot Password with Valid email")
@allure.tag("Functional")
@allure.label("owner", "Dhruvil Patel")
@allure.testcase("TC#3")
@pytest.mark.Functional

def test_post_forgot_password_valid_email():
    base_url = "https://savvy-valet.concettoprojects.com/savvy-valet-api/public/api"
    base_path = "/forgot-password"
    URL = base_url + base_path
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    form_data = {

        "email": "dhruvil.patel+9999@concettolabs.com"
    }

    responseData = requests.post(URL, data=form_data, headers=headers)
    assert responseData.status_code == 200
    response = responseData.json()

    if "email" in responseData:
        email = responseData['email']
        assert email == "dhruvil.patel+9999@concettolabs.com" , f"Expected email to be 'dhruvil.patel+9999@concettolabs.com', but got {email}'"

@allure.title("Test Post Request - Savvy Wallet Project")
@allure.description("TC#4 - Verify the Forgot Password with Valid Capital email")
@allure.tag("Functional")
@allure.label("owner", "Dhruvil Patel")
@allure.testcase("TC#4")
@pytest.mark.Functional

def test_post_forgot_password_valid_Capital_email():
    base_url = "https://savvy-valet.concettoprojects.com/savvy-valet-api/public/api"
    base_path = "/forgot-password"
    URL = base_url + base_path
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    form_data = {

        "email": "DHRUVIL.PATEL+9999@CONCETTOLABS.COM"
    }

    responseData = requests.post(URL, data=form_data, headers=headers)
    assert responseData.status_code == 200
    response = responseData.json()

    if "email" in responseData:
        email = responseData['email']
        assert email == "DHRUVIL.PATEL+9999@CONCETTOLABS.COM" , f"Expected email to be 'dhruvil.patel+9999@concettolabs.com', but got {email}'"


@allure.title("Test Post Request - Savvy Wallet Project")
@allure.description("TC#5 - Verify the Forgot Password with InValid format email")
@allure.tag("Functional")
@allure.label("owner", "Dhruvil Patel")
@allure.testcase("TC#5")
@pytest.mark.Functional
def test_post_forgot_password_valid_Capital_email():
    base_url = "https://savvy-valet.concettoprojects.com/savvy-valet-api/public/api"
    base_path = "/forgot-password"
    URL = base_url + base_path
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    form_data = {

        "email": "dhruvil.patel@ifdsfkosdjf"
    }

    responseData = requests.post(URL, data=form_data, headers=headers)
    assert responseData.status_code == 422
    response = responseData.json()

    if "email" in responseData:
        email = responseData['email']
        assert email == "dhruvil.patel@ifdsfkosdjf", f"Expected email to be 'dhruvil.patel+9999@concettolabs.com', but got {'The email field format is invalid'}'"

