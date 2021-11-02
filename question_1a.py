
""" Question 1a

    This is unoptimized and coupled solution

    Using python built-in module date and calendar

    Nested loop increase time complexity
"""

import calendar
from datetime import date

sunday = 0

for y in range(1901, 2001):
    
    sun_text = calendar.TextCalendar(calendar.SUNDAY)
    
    for m in range(1, 13):
        for k in sun_text.itermonthdays(y, m):
            if k!=0:
                day = date(y, m, k)
                if day.weekday() == 6:
                    sunday += 1

print(sunday)