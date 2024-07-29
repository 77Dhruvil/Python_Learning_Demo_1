# Integration Scenarios

# 1 Verify that create booking -> patch Request -> Verify that Firstname is Updated.
# 2 Create a booking , Delete the booking with id and Verify Using Get Request it should not exist.
# 3 Get an Existing Booking id from get all Booking id , update a Booking and Verify using Get By id.
# 4 Create Booking , Delete it
# 5 Invalid Creation - Enter a wrong payload or a Wrong JSON
# 6 Trying to update on Delete ID -> 404


# Test for Single Req
# 1 Response
# 2 Status Code
# 3 Headers

# Add assertations for the negative test case (always)

# -----------------------------------------------------------------------------------------------------------------
# Fixture Concept -> Python
# You can use this Fixture
# Context to the test
# Similar - pre condition , post condition

# PreCondition - token , booking id  - Fixture
# test_update negative 1
# test_update positive 2


# Set up and TearDown - Pre-condition and post-condition
#
# import pytest
#
#
# @pytest.fixture()
# def is_married():
#     return True
#
#
# def test_i_need_confirm(is_married):
#     assert is_married == True
# import pytest
#
# @pytest.fixture()
# def Sample_data ():
#     data = [1,2,3,4,5]
#     return data
#
# @pytest.fixture()
# def Sample_data1 ():
#     return True
#
# @pytest.mark.regression
# def test_consume_sameple1_sample2(Sample_data,Sample_data1):
#     print(Sample_data)
#     print(Sample_data1)


import pytest
import requests
import allure


def test_Consume_data_1_2(create_token, create_booking_id):
    print(create_token)
    booking_id = create_booking_id
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(booking_id)
    PUT_url = base_url + base_path
    cookie = "token=" + create_token
    headers = {"Content-Type": "application/json", "Cookie": cookie}
    # Rest of your code...

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

    response = requests.put(url=PUT_url, headers=headers, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["firstname"] == "Devil"


def test_Consume_data_1_21(create_token, create_booking_id):
    print(create_token)
    print(create_booking_id)
