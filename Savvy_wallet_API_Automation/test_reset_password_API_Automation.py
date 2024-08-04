import allure
import pytest
import requests


@allure.title("Test Post Request - Savvy Wallet Project")
@allure.description("TC#1 - Verify the Reset Password with Empty fields")
@allure.tag("Functional")
@allure.label("owner", "Dhruvil Patel")
@allure.testcase("TC#1")
@pytest.mark.Functional
def test_post_Reset_password_Empty_field():
    base_url = "https://savvy-valet.concettoprojects.com/savvy-valet-api/public/api"
    base_path = "/reset-password"
    URL = base_url + base_path
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    form_data = {
         "email": "",
         "new_password" : "",
         "confirm_password" : ""
    }

    responseData = requests.post(URL, data=form_data, headers=headers)
    assert responseData.status_code == 422
    response = responseData.json()

    if "email" in responseData:
        email = responseData['email']
        assert email == "", f"Expected email to be 'dhruvil.patel+9999@concettolabs.com', but got {'The email field is required'}'"

    if "new_password" in responseData:
        new_password = responseData['new_password']
        assert new_password == "", f"Expected new_password to be 'Test@1234', but got {'The new password field is required'}'"

    if "confirm_password" in responseData:
        confirm_password = responseData['confirm_password']
        assert confirm_password == "", f"Expected confirm_password to be 'Test@1234', but got {'The confirm password field is required'}'"