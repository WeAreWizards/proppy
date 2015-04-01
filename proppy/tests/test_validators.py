from proppy.validators import (
    is_currency,
    is_date,
    is_percentage,
    is_present,
    are_valid_deliverables,
    are_valid_rates
)


def test_is_present():
    assert is_present(None) is False
    assert is_present("") is False
    assert is_present([]) is False

    assert is_present("hey") is True
    assert is_present(2) is True


def test_is_percentage():
    assert is_percentage(None) is False
    assert is_percentage(42) is True
    assert is_percentage(3.14) is True


def test_is_currency():
    assert is_currency(None) is False
    assert is_currency("pounds") is False
    assert is_currency("£") is True


def test_is_date():
    # strict validation
    strict_date_validator = is_date()
    assert strict_date_validator("") is False
    # no american weird notation
    assert strict_date_validator("2015/30/01") is False
    assert strict_date_validator("2015/01/30") is True

    # optional dates
    optional_date_validator = is_date(optional=True)
    assert optional_date_validator(None) is True
    assert strict_date_validator("2015/01/30") is True


def test_are_valid_rates():
    no_amount_rate = {'name': 'invalid'}
    no_name_rate = {'amount': 20}
    valid_rate = {'name': 'valid', 'amount': 20}
    assert are_valid_rates([no_amount_rate]) is False
    assert are_valid_rates([no_name_rate]) is False
    assert are_valid_rates([valid_rate, valid_rate]) is False
    assert are_valid_rates([valid_rate]) is True


def test_are_valid_deliverables():
    missing_field_deliverable = {'name': 'invalid'}
    valid_deliverable = {
        'name': 'Fix Facebook and Twitter integration',
        'estimate': 1,
        'rate': 'dev',
        'free': False,
        'description': 'Ensure those are working properly for login '
    }
    assert are_valid_deliverables([missing_field_deliverable]) is False
    assert are_valid_deliverables([valid_deliverable]*2) is False
    assert are_valid_deliverables([valid_deliverable]) is True
