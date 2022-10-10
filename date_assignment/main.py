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

# array input similar method
dates = [x if x.isdigit() else "illegal" for x in stdin.readlines() if x.isdigit()]

print(dates)

for date in dates[1:]:
    if date == "illegal":
        print("Line {}: illegal".format(n))
    elif check_date(date[2:4],date[:2],date[4:]):
        prev_date = date[n-1]

        if datetime.strptime(date, "%d%m%Y").date() < datetime.strptime(prev_date, "%d%m%Y").date():
            print("Line {}: older".format(n))
    else:
        dates[n] = "illegal"
    
    n += 1
