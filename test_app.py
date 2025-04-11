from app import get_tide_status


def test_high_tide():
    assert get_tide_status(0) == "High Tide"
    assert get_tide_status(6) == "High Tide"
    assert get_tide_status(12) == "High Tide"
    assert get_tide_status(18) == "High Tide"


def test_low_tide():
    assert get_tide_status(3) == "Low Tide"
    assert get_tide_status(9) == "Low Tide"
    assert get_tide_status(15) == "Low Tide"
    assert get_tide_status(21) == "Low Tide"


def test_mid_tide():
    assert get_tide_status(1) == "Mid Tide"
    assert get_tide_status(7) == "Mid Tide"
