import sys

for line in sys.stdin:
    a, b, c = (int(s)%360 for s in line.split())
    if c < b:
        c = c + 360

    if b <= a <= c:
        sys.stdout.write('TRUE' + '\n')
    elif b == c:
        sys.stdout.write('TRUE' + '\n')
    else:
        sys.stdout.write('FALSE' + '\n')