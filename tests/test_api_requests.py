import requests
import json
from assertpy.assertpy import assert_that


def test_get_bookingIds(app_config):
# We use requests.get() with url to make a get request
    response = requests.get(app_config.base_url)
# we can assert on the response status code
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

def test_create_booking(app_config):
#Creeate the JSON with the data of the new booking
    pData = {"firstname" : "Daniel",
             "lastname" : "Baltodano",
             "totalprice" : 1500,
             "depositpaid" : True,
             "bookingdates" :
                 {"checkin" : "2023-01-01",
                  "checkout" : "2023-07-07"},
             "additionalneeds" : "Breakfast"}
#Create a new booking
    response = requests.post(app_config.base_url,
                             data=json.dumps(pData),
                             headers={"Content-Type": "application/json"})
# we can assert on the response status code
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

def test_get_bookingById(app_config):
#We declare the variable for the id under test
    id = 1
    id = str(id)
#We create the URL for the test with the given ID
    req = app_config.base_url + id
# We use requests.get() with url to make a get request
    response = requests.get(req)
# response from requests has many useful properties
# we can assert on the response status code
    assert_that(response.status_code).is_equal_to(requests.codes.ok)


def test_delete_booking(app_config):
    # We declare the variable for the id under test
    id = 1
    id = str(id)
    # We create the URL for the test with the given ID
    req = app_config.base_url + id
    response = requests.delete(req)