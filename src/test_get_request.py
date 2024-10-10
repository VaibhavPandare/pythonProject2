import pytest
import allure
import requests

@allure.title("Test Get Request-Restful Booker ")
@allure.description("TC#1 -> Verify that GET Request works with ID ")
@allure.tag("regression","smoke")
@allure.label("Owner","Vaibhav Panadare")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url="https://restful-booker.herokuapp.com/booking/4519"
    response_data=requests.get(url)
    print(response_data.json())
    assert response_data.status_code==200


