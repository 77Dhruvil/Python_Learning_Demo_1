import allure
import pytest
import requests
@allure.feature('Booking')
@allure.title("Create Booking")
@allure.description("TC#1 Verify that user is able to create booking")
@allure.tag("Functional")
#@allure.mark.CRUD
def test_create_booking_positive():
     #To Make a post Request
    #URL -
    #Header - content-type=Application/json
    #method - Post
    #payload - Dict / JSON
    #Auth (NO)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    Total_url = base_url + base_path
    headers = {"content_Type" : "application/json"}
    payload = {

        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=Total_url,headers=headers,json=payload)
    assert response.status_code == 200, "Booking is not created"
    responseData = response.json()

    assert responseData["bookingid"] != None, "Booking id is null"
    assert responseData["bookingid"] > 0, "Booking id is not greater than 0"
    assert type(responseData["bookingid"]) == int, "Booking id is not an integer"
    firstname = responseData ["booking"] ["firstname"]
    assert firstname == "Jim"
    checkin = responseData["booking"]["bookingdates"]["checkin"]
    assert checkin == "2018-01-01"