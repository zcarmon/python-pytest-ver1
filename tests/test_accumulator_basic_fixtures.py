from pages.accumulator import Accumulator
import pytest

@pytest.fixture
def acm(scope="module"):
    return Accumulator()

def test_acm_creation(acm):
    assert acm.count == 0

def test_acm_creation_twice(global_acm):
    global_acm.add_counts()
    global_acm.add_counts(1)
    assert global_acm.count == 2

def test_acm_creation_10(acm):
    acm.add_counts(5)
    assert acm.count == 5