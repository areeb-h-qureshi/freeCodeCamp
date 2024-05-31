def add_time(start, duration, *weekday):
    start24h = milTime(start)
    future = forward(start24h, duration)
    new_clock = future[0]
    days_passed = future[1]
    final_clock = regTime(new_clock)
    final_weekday = ""
    if weekday:
        final_weekday = calDay(weekday[0].capitalize(), days_passed)
    final_text = ""
    if days_passed == 1:
        final_text = " (next day)"
    elif days_passed > 1:
        final_text = f" ({days_passed} days later)"

    new_time = f"{final_clock}{final_weekday}{final_text}"
    return new_time


def milTime(time12h):
    xx = time12h.split()
    clock = xx[0]
    meridiam = xx[1]
    if meridiam == "AM":
        return clock
    elif meridiam == "PM" and clock == "12:00":
        return clock
    elif meridiam == "PM":
        yy = clock.split(":")
        yy[0] = str(int(yy[0]) + 12)
        clock = ":".join(yy)
        return clock


def forward(time24, duration):
    aa = time24.split(":")
    bb = duration.split(":")
    original_hour = int(aa[0])
    original_min = int(aa[1])
    dur_hour = int(bb[0])
    dur_min = int(bb[1])

    hours_passed = 0
    days_passed = 0

    new_min = original_min + dur_min
    if new_min >= 60:
        hours_passed = new_min // 60
        new_min = new_min % 60

    new_hour = original_hour + dur_hour + hours_passed
    if new_hour >= 24:
        days_passed = new_hour // 24
        new_hour = new_hour % 24

    new_clock24h = "{0}:{1:0>2d}".format(new_hour, new_min)
    return (new_clock24h, days_passed)


def regTime(time12h):
    meridiam = " AM"
    zz = time12h.split(":")
    if int(zz[0]) >= 12:
        meridiam = " PM"
        zz[0] = str(int(zz[0]) - 12)
    if int(zz[0]) == 0:
        zz[0] = "12"
    res = ":".join(zz)
    res += meridiam
    return res


def calDay(weekday, days_passed):
    week = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    day_number = week.get(weekday)
    day_number += days_passed
    day_number %= 7
    week_string = {}
    for k, v in week.items():
        week_string[v] = k
    day_string = week_string.get(day_number)
    final_day = f", {day_string}"
    return final_day

