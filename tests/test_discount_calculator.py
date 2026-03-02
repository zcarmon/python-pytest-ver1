import json
import pytest
from assertpy import assert_that

# Loads the params from a json file
def load_params_from_json():
    with open('tests/json_calc_data.json','r') as f:
        the_params = json.load(f)
        return [(item['price'], item ['discount'], item['result']) for item in the_params]

# invoke the calc function with the parameterized fixture
@pytest.mark.api
@pytest.mark.parametrize("price,discount,result", load_params_from_json())
def test_calculate_discount(price,discount,result):
    the_res = calculate_discount(price, discount)
    print(f'The price {price} after discount of {discount}% is {result}')
    # assert the_res == result
    assert_that(calculate_discount(price,discount)).is_equal_to(result)

def calculate_discount(price, discount) -> float:
    if price <= 0 or discount <= 0:
        pytest.raises(ValueError, ("The price and discount must be positive number!"))
    return price * (1 - discount / 100)

# def test_calculate_discount():
#     print(calculate_discount(100, 10))