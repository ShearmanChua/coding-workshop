# You are given a list of up to N dates via stdin with ddmmyyyy on each line, where dd represents the day, mm represents the month and yyyy represents the year.

# Input Format

# Each line is guaranteed to contain 8 characters followed by an end of line character \n, but not guaranteed to be legal. A legal date is a valid Gregorian calendar date consisting of only the digits 0 to 9.

# And all dates before 1 Jan 1600 are also considered illegal.

# Constraints

# 1 <= N <= 1,000,000

# Output Format

# For line number n (n starts from 1),

# print "Line n: Illegal" if the date is not legal.

# print "Line n: Older" if the date is legal and older than the date on previous line n-1, if any.

# A legal date will not be considered older than an illegal date.

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

n = 1


dates = [date for date in stdin.readlines()]
prev_illegal = not check_date(dates[0][2:4],dates[0][:2],dates[0][4:-1]) or not dates[0][:-1].isdigit() or not(int(dates[0][4:-1]) >= 1600)

if prev_illegal:
     print("Line {}: Illegal".format(n))

for date in dates[1:]:

    if not date[:-1].isdigit():
        print("Line {}: Illegal".format(n+1))
        prev_illegal = True
    
    elif check_date(date[2:4],date[:2],date[4:-1]) and int(date[4:-1])>=1600:
        prev_date = dates[n-1]

        if not prev_illegal and datetime.datetime.strptime(date[:-1], "%d%m%Y").date() < datetime.datetime.strptime(prev_date[:-1], "%d%m%Y").date():
            print("Line {}: Older".format(n+1))
        
        prev_illegal = False
    else:
        print("Line {}: Illegal".format(n+1))
        prev_illegal = True
    
    n += 1
