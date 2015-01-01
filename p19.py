weekdays = {
  0 : 'Monday',
  1 : 'Tuesday',
  2 : 'Wednesday',
  3 : 'Thursday',
  4 : 'Friday',
  5 : 'Saturday',
  6 : 'Sunday',
}

def monthlengths(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                february = 29
            else:
                february = 28
        else:
            february = 29
    else:
        february = 28

    lengths = {
      1  : 31,
      2  : february,
      3  : 31,
      4  : 30,
      5  : 31,
      6  : 30,
      7  : 31,
      8  : 31,
      9  : 30,
      10 : 31,
      11 : 30,
      12 : 31,
    }
    return lengths

def make_map():
    daymap = []
    dayind  = 0
    year    = 1900

    while year <= 2000:
        month = 1
        while month <= 12:
            numdays = monthlengths(year)[month]
            day = 1
            while day < numdays:
                daymap.append({
                  'year'   : year,
                  'month'  : month,
                  'day'    : day,
                  'weekday': weekdays[dayind % 7],
                })
                day += 1
                dayind += 1
            month += 1
        year += 1
    return daymap[365:]

def count_sundays():
    daylist = make_map()
    sundays = 0
    for day in daylist:
        if day['day'] == 1 and day['weekday'] == 'Sunday':
            sundays += 1
    return sundays

print count_sundays()
