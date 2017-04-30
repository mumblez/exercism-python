from datetime import date
from calendar import monthrange, day_name

def meetup_day(year, month, dayofweek, request):
    dayMap = {day_name[n]: n for n in range(7)}
    possibleDays = [day for day in range(1, monthrange(year, month)[1]+1) if date(year, month, day).weekday() == dayMap[dayofweek]]

    if request == 'last':
        return date(year, month, possibleDays[-1])
    elif request == 'teenth':
        if possibleDays[0] < 3:
            return date(year, month, possibleDays[2])
        else:
            return date(year, month, possibleDays[1])
    else:
        req = int(request[:1])
        if req <= len(possibleDays):
            return date(year, month, possibleDays[req-1])
        else:
            raise MeetupDayException("Day not found")
