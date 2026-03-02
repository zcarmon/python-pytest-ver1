import pytest
from pages.accumulator import Accumulator

@pytest.fixture
def global_acm():
    return Accumulator()