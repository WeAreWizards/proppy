import datetime


def get_work_days_interval(start, end):
    """
    Find out the number of working days for the interval
    between the 2 given dates
    """
    start = datetime.datetime.strptime(start, "%Y/%m/%d")
    end = datetime.datetime.strptime(end, "%Y/%m/%d")
    total_days = (end - start).days
    working_days = 0
    day = start
    for _ in range(total_days):
        day = day + datetime.timedelta(days=1)
        # 6 -> saturday, 7 -> sunday
        if day.isoweekday() not in [6, 7]:
            working_days += 1

    return working_days
