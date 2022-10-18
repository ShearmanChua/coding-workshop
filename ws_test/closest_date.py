'''Closest date 2'''

# You are given a list of up to N dates via stdin with YYYYMMDD on each line, where DD represents the day, MM represents the month and YYYY represents the year.
from sys import stdin, stdout
import datetime
import bisect

def check_date(m, d, y):
    try:
        m, d, y = map(int, (m, d, y))
        datetime.date(y, m, d)
        return True
    except ValueError:
        return False

def minimumAbsoluteDifference(arr):
    return min(arr[i+1].date()-arr[i].date() for i in range(len(arr)-1))

def new_delta(date_list,pos):
    if 0 < pos < len(date_list) - 1:
        return min([date_list[pos+1].date()-date_list[pos].date(),date_list[pos].date()-date_list[pos-1].date()])
    elif pos == 0:
        return(date_list[pos+1].date()-date_list[pos].date())
    else:
        return(date_list[pos].date()-date_list[pos-1].date())

dates = stdin.readlines()
legal_dates =  []

if check_date(dates[0][4:6],dates[0][6:-1],dates[0][:4]) and int(dates[0][:4])>=1600:
    legal_dates.append(datetime.datetime.strptime(dates[0][:-1], "%Y%m%d"))

print("4000000")
last_output = None

for idx,date in enumerate(dates[1:]):
    if check_date(date[4:6],date[6:-1],date[:4]) and int(date[:4])>=1600:
       
        # legal_dates.append(datetime.datetime.strptime(date[:-1], "%Y%m%d"))
        pos_to_insert = bisect.bisect(legal_dates, datetime.datetime.strptime(date[:-1], "%Y%m%d"))
        legal_dates.insert(pos_to_insert,datetime.datetime.strptime(date[:-1], "%Y%m%d"))

        if len(legal_dates)>1:

            smallest_delta = abs(int(new_delta(legal_dates,pos_to_insert).days))

            if last_output == None:
                print(smallest_delta)
                last_output = smallest_delta
            elif smallest_delta < last_output:
                print(smallest_delta)
                last_output = smallest_delta
