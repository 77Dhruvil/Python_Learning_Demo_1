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

    bookingid = responseData["bookingid"]
    assert responseData["bookingid"] != None, "Booking id is null"
    assert responseData["bookingid"] > 0, "Booking id is not greater than 0"
    assert type(responseData["bookingid"]) == int, "Booking id is not an integer"
    firstname = responseData ["booking"] ["firstname"]
    lastname = responseData ["booking"] ["lastname"]
    totalprice = responseData ["booking"] ["totalprice"]
    depositpaid = responseData ["booking"] ["depositpaid"]
    additionalneeds = responseData ["booking"] ["additionalneeds"]
    assert firstname == "Jim"
    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == True
    assert additionalneeds == "Breakfast"
    checkin = responseData["booking"]["bookingdates"]["checkin"]
    assert checkin == "2018-01-01"



@allure.title("Create Booking CRUD")
@allure.description("TC#2 Verify that user is able to create booking is not with {} data")
#@allure.mark.CRUD
def test_Create_booking_negative_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    Total_url = base_url + base_path
    headers = {"content-Type : application/json"}
    payload = {}
    response = requests.post(url=Total_url , headers=headers , json=payload)
    print(type(Total_url))
    print(type(headers))
    print(type(payload))
    assert response.status_code == 500, "Booking is created with invalid data"


@allure.title("Create Booking CRUD")
@allure.description("TC#3 Verify Booking with Total price string Negative")
#@allure.mark.CRUD
def test_Create_booking_negative_tc2():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    Total_url = base_url + base_path
    headers = {"content-Type : application/json"}
    payload = {

        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": "saofkspfdk",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=Total_url , headers=headers , json=payload)
    response = response.json()
    totalprice = response["booking"][ "totalprice"]
    assert totalprice == 111
    assert response.status_code == 500, "Booking is created with invalid data"