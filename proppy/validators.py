import datetime


def is_present(value):
    """
    Check that the value provided exists, 0 is a potential
    good value so we can't use check falsyness
    """
    return value is not None and value != "" and value != []
is_present.message = "Field %s is missing"


def is_percentage(value):
    """
    0 is a pretty useless percentage in a proposal
    so counting it as falsy
    """
    if value is None or type(value) is str:
        return False
    return 0 < value <= 100
is_percentage.message = "Field %s is not a valid percentage"


def is_currency(value):
    """
    List of currencies hardcoded for now since we need to know
    how to format it
    """
    return value in ["£", "$", "€"]
is_currency.message = "Field %s is not a supported currency"


def is_date(optional=False):
    """
    Checks whether the value is a date formatted YYYY/MM/DD
    """
    def check_date(value):
        if optional and value is None:
            return True

        try:
            datetime.datetime.strptime(value, "%Y/%m/%d")
        except ValueError:
            return False

        return True
    check_date.message = "Field %s is not a valid date (should be YYYY/MM/DD)"

    return check_date


def are_valid_rates(rates):
    """
    A rate has a name and an amount (int) and no rate
    should be duplicated
    """
    rate_names = []
    required = ['name', 'amount']
    for rate in rates:
        if (
            any(field not in rate for field in required) or
            int(rate['amount']) <= 0 or
            rate['name'] in rate_names
        ):
            return False
        rate_names.append(rate['name'])
    return True
are_valid_rates.message = "Field %s contains invalid rates"


def are_valid_deliverables(deliverables):
    """
    A deliverable should have a name, a description, an estimate
    and a rate.
    No deliverable should be duplicated
    """
    deliverable_names = []
    required = ['name', 'description', 'estimate', 'rate', 'free']
    for deliverable in deliverables:
        if (
            any(field not in deliverable for field in required) or
            float(deliverable['estimate']) <= 0 or
            deliverable['name'] in deliverable_names
        ):
            return False
        deliverable_names.append(deliverable['name'])
    return True
are_valid_deliverables.message = "Field %s contains invalid deliverables"
