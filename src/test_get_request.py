import pytest
import allure
import requests

@allure.title("Test Get Request-Restful Booker ")
@allure.description("TC#1 -> Verify that GET Request works with valid ID ")
@allure.tag("regression","smoke")
@allure.label("Owner","Vaibhav Panadare")
@allure.testcase("TC#1")
def test_get_single_request_by_id_positive():
    url="https://restful-booker.herokuapp.com/booking/1"
    response_data=requests.get(url)
    print(response_data.json())
    assert response_data.status_code==200


@allure.title("Test Get Request-Restful Booker ")
@allure.description("TC#2 -> Verify that GET Request works with not present ID ")
@allure.testcase("TC#2")
def test_get_single_request_by_id_negative1():
    url="https://restful-booker.herokuapp.com/booking/111123"
    response_data=requests.get(url)
    print(response_data.json())
    assert response_data.status_code==404

@allure.title("Test Get Request-Restful Booker ")
@allure.description("TC#3 -> Verify that GET Request works with negative ID ")
@allure.testcase("TC#3")
def test_get_single_request_by_id_negative2():
    url="https://restful-booker.herokuapp.com/booking/-678"
    response_data=requests.get(url)
    print(response_data.json())
    assert response_data.status_code==404

@allure.title("Test Get Request-Restful Booker ")
@allure.description("TC#4 -> Verify that GET Request works with invalid ID ")
@allure.testcase("TC#4")
def test_get_single_request_by_id_negative3():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    response_data = requests.get(url)
    print(response_data.json())
    assert response_data.status_code==404