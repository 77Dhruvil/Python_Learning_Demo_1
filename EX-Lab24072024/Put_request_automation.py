#PUT
#URL
#PATH - BOOKING ID
#Token - AUTH
#Payload
import pytest
import allure
import requests

def create_token():
   url = "https://restful-booker.herokuapp.com/auth"
   headers = {"Content-Type" :"application/json"}
   payload = {
     "username" : "admin",
    "password"  : "password123"
   }
   response = requests.post(url=url , headers = headers , json = payload)
   token = response.json()["token"]
   print(token)
   return token

def create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    Total_url = base_url + base_path
    headers = {"content_Type": "application/json"}
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
    response = requests.post(url=Total_url, headers=headers, json=payload)
    assert response.status_code == 200, "Booking is not created"
    data = response.json()
    booking_id = data["bookingid"]
    print(booking_id)
    return booking_id

def test_put_request_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+str(create_booking())
    PUT_url = base_url + base_path

    cookie = "token=" + create_token()
    headers = {"content_Type": "application/json", "Cookie": cookie}



    payload = {

        "firstname": "Devil",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=PUT_url , headers=headers , json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data ["firstname"] == "Devil"