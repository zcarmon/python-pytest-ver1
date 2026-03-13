import requests
import pytest
from assertpy import assert_that
from dotenv import load_dotenv
import os

load_dotenv()
base_url = "https://reqres.in/api/"

def test_get_user_by_id():
    url = f"{}users?page=2"
    headers = {
        'x-api-key': os.getenv("X_API_KEY")
    }

    # ביצוע הבקשה (GET Request)
    response = requests.get(url, headers=headers)

    resp_body = response.json()
    print(resp_body)
    assert response.status_code == 200
    # assert resp_body["data"][1]["id"] == 2
    obj = resp_body["data"]
    for x in obj:
        #print(x["data"]["id"])
        print(x["id"])

    assert_that(resp_body["data"][2]["id"]).is_equal_to(9)
    assert(response.ok)
    print('The url is = ' ,response.url)
