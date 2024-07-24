#GET Request BookingID
#URL  https://restful-booker.herokuapp.com/booking/1
#Auth? X
#Payload? X
#Content-type or Header? X
#Query param ? X
#path param - 1

#Response
#Body - Verify - Assert , #Keys,Value
#Status Code - Verify
#Time
#Json Schema , XML Schema



import pytest
import allure
import requests
@allure.title("Test Get Request of Restful Booker Project#1")
@allure.description("Verify that get request with ID Works")
@allure.tag("Regression" , "Smoke")
@allure.label("owner" , "Dhruvil")
@allure.testcase("TC#1")
@pytest.mark.regression
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.json())
    assert  responseData.status_code == 200, "Status Code is not 200"
  #  assert responseData.json()["firstname"] == "Dhruvil", "First Name is not Correct"
  #  assert responseData.json()["lastname"] == "Patel", "Last Name is not Correct"
  #  assert responseData.json()["totalprice"] == 111, "Total Price is not Correct"
  #  assert responseData.json()["depositpaid"] == True, "Deposit Paid is not Correct"
  #  assert responseData.json()["bookingdates"]["checkin"] == "2018-01-01", "Check In Date is not Correct"
  #  assert responseData.json()["bookingdates"]["checkout"] == "2019-01-01", "Check Out Date is not Correct"
  #  assert responseData.json()["additionalneeds"] == "Breakfast", "Additional Needs is not Correct"
@allure.title("Test Get Request of Restful Booker Project#1")
@allure.description("TC#2Verify that get request with Invalid Booking ID")
@pytest.mark.regression
def test_get_single_request_by_id_Negative():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    responseData = requests.get(url)
    assert responseData.status_code == 404, "Status Code is not 404"

@allure.title("Test Get Request of Restful Booker Project#1")
@allure.description("TC#3Verify that get request with  Booking ID")
@pytest.mark.regression
def test_get_single_request_by_id_Negative2():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    assert responseData.status_code != 200, "Status Code is not 404"


@allure.title("Test Get Request of Restful Booker Project#1")
@allure.description("TC#4Verify that get request with  Booking ID")
@pytest.mark.regression
def test_get_single_request_by_id_Negative3():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.json())
    print(responseData.status_code)
    print(responseData.headers)
    print(responseData.url)
    print(responseData.cookies)
    print(responseData.text)
    assert responseData.status_code == 200, "Status Code is not 404"
