from sys import stdin, stdout
import re
import datetime

def check_date(m, d, y):
    try:
        m, d, y = map(int, (m, d, y))
        datetime.date(y, m, d)
        return True
    except ValueError:
        return False

def minimumAbsoluteDifference(arr):
    return min(arr[i+1].date()-arr[i].date() for i in range(len(arr)-1))

dates = stdin.readlines()
legal_dates =  [datetime.datetime.strptime(date[:-1], "%Y%m%d") for date in dates if date[:-1].isdigit() and check_date(date[4:6],date[6:-1],date[:4]) and int(date[:4])>=1600]

if len(legal_dates)>1:

    legal_dates = sorted(legal_dates)

    smallest_delta = abs(int(minimumAbsoluteDifference(legal_dates).days))

    print(smallest_delta)

else:
    print(-1)
