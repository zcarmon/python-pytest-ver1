import json

import pytest
from assertpy import assert_that

def test_example4():
    assert (2 + 4 == 6) == True

def test_substr():
    a = "asas"
    b = "asas"
    assert_that(a). contains(b)

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 2 / 0
    assert "division by zero" in str(e.value)

params = [(1,2,3),(2,2,4),(5,5,10)]

def load_params_from_json():
    with open('tests/json_data.json','r') as f:
        params2 = json.load(f)
        return [(item['x'], item ['y'], item['result']) for item in params2]


@pytest.mark.parametrize("x,y,result", load_params_from_json())
def test_add(x,y,result):
    assert x + y == result
    assert_that(x + y).is_equal_to(result)