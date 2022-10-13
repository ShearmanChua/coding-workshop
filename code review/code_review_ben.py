import sys

for line in sys.stdin:
    a, b, c = (int(s)%360 for s in line.split())

    # I think line 7 and 8 not needed? I tried it without and it passed the 'Run Code' cause modulo negative number returns postive 
    # number. There is no need to add 360 to c. Cause if not -3 0 -2 which I tested would have failed 0 <= -3 <= 358
    if c < b:
        c = c + 360 

    if b <= a <= c: # if a in range(b,c+1)
        sys.stdout.write('TRUE' + '\n')
    elif b == c:
        sys.stdout.write('TRUE' + '\n')
    else:
        sys.stdout.write('FALSE' + '\n')