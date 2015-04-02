import datetime


def to_date(date):
    """
    Returns a datetime given a string of the YYYY/MM/DD format
    """
    return datetime.datetime.strptime(date, "%Y/%m/%d")


def get_work_days_interval(start, end):
    """
    Find out the number of working days for the interval
    between the 2 given dates
    """
    total_days = (end - start).days
    working_days = 0
    day = start
    for _ in range(total_days):
        day = day + datetime.timedelta(days=1)
        # 6 -> saturday, 7 -> sunday
        if day.isoweekday() not in [6, 7]:
            working_days += 1

    return working_days
