import pytest
import requests
import allure


@pytest.fixture()
def create_token():
    print("Create a token")
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=payload)
    token = response.json()["token"]
    print(token)
    return token

print("hello world1")
@pytest.fixture()
def create_booking_id():
    print("Create a Booking ID")
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
    return response.json()["booking id"]


@pytest.fixture
def launch_browser():
    print("Launching a Chrome Browser")
    return "Chrome"
@pytest.fixture
def read_mysql_file_databse():
    pass

@pytest.fixture
def read_url_testdata_excel():
    pass

def close_browser():
    print("Clossing a Chrome Browser")
    return "Closed"