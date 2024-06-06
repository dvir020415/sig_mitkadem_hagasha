def gen_secs():
    # Generator for seconds (0-59)
    for sec in range(60):
        yield sec

def gen_minutes():
    # Generator for minutes (0-59)
    for minute in range(60):
        yield minute

def gen_hours():
    # Generator for hours (0-23)
    for hour in range(24):
        yield hour

def gen_time():
    # Generator for time in the format HH:MM:SS
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, sec)

def gen_years(start=2024):
    # Generator for years starting from a given year (default 2024)
    year = start
    while True:
        yield year
        year += 1

def gen_months():
    # Generator for months (1-12)
    for month in range(1, 13):
        yield month

def gen_days(month, leap_year=True):
    # Function to return the number of days in a given month
    # Takes into account leap years for February
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month == 2:
        return 29 if leap_year else 28
    else:
        return 30

def gen_date():
    # Generator for full date and time in the format DD/MM/YYYY HH:MM:SS
    for year in gen_years():
        leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        for month in gen_months():
            days_in_month = gen_days(month, leap_year)
            for day in range(1, days_in_month + 1):
                for hour_minute_sec in gen_time():
                    yield "%02d/%02d/%d %s" % (day, month, year, hour_minute_sec)

# Create an iterator for the gen_date generator
gen_date_iter = gen_date()

# Advance the iterator 1,000,000 times to skip ahead in the date sequence
for _ in range(1000000):
    next(gen_date_iter)

# Print the next date in the sequence after the skipped dates
print(next(gen_date_iter))
