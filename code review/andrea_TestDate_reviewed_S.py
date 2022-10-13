import re
import datetime
import math #pylint: Unused import math (unused-import)
from math import nan
import fileinput

file = fileinput.input()
row = 1
for line in file:
    line = line.strip()
    all_digits = bool(re.match('^[0-9]+$', line))
    
    if all_digits == False: #pylint: Comparison 'all_digits == False' should be 'all_digits is False' if checking for the singleton value False, or 'not all_digits' if testing for falsiness (singleton-comparison)
        print(f'Line {row}: Illegal')
        prev = nan
        row += 1
        continue

    day = int(line[:2])
    month = int(line[2:4])
    year = int(line[4:])
    
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        print(f'Line {row}: Illegal')
        prev = nan
        row += 1
        continue

    if year < 1600:
        print(f'Line {row}: Illegal')
        prev = nan
        row += 1
        continue
    elif row != 1: #pylint: Unnecessary "elif" after "continue", remove the leading "el" from "elif" (no-else-continue)
        current = datetime.datetime.strptime(line, '%d%m%Y')
        if isinstance(prev, datetime.datetime):
            if (current < prev):  # pylint: Unnecessary parens after 'if' keyword
                print(f'Line {row}: Older')
                
    row += 1
    prev = datetime.datetime.strptime(line, '%d%m%Y')
        