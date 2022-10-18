'''Find X Value'''

# Find the value of x
# one "="
# 3 numbers A, B and x (A and B are known, while x is unknown)
# one operator (+, -, *, or /) between 2 of the 3 numbers
from curses.ascii import isalnum
from sys import stdin, stdout
from decimal import Decimal
import math

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

def divide(dividend, divisor):
    return int(dividend)/int(divisor)

def multiply(A, B):
    return int(A)*int(B)
def add(A, B):
    return int(A) + int(B)
def minus(left, right):
    return int(left) - int(right)

for equation in stdin.readlines():
    # print(equation)
    lhs =  equation.strip().split("=")[0]
    rhs = equation.strip().split("=")[1]

    if 'x' in lhs:
        if lhs.isalnum():
            if '/' in rhs:
                ans = divide(rhs.split("/")[0],rhs.split("/")[1])
            elif '*' in rhs:
                ans = multiply(rhs.split("*")[0],rhs.split("*")[1])
            elif '+' in rhs:
                ans = add(rhs.split("+")[0],rhs.split("+")[1])
            else:
                ans = minus(rhs.split("-")[0],rhs.split("-")[1])
        else:
            if '/' in lhs:
                if lhs.split('/')[0] == 'x':
                    ans =  multiply(rhs,lhs.split('/')[1])
                else:
                    ans = divide(lhs.split('/')[0],rhs)
            elif '*' in lhs:
                ans = divide(rhs, lhs.replace('x','').replace('*',''))
            elif '+' in lhs:
                ans = minus(rhs,lhs.replace('x','').replace('+',''))
            else:
                if lhs.split('-')[0] == 'x':
                    ans = add(lhs.split('-')[1],rhs)
                else:
                    ans = minus(lhs.split('-')[0],rhs)
    else:
        if rhs.isalnum():
            if '/' in lhs:
                ans = divide(lhs.split("/")[0],lhs.split("/")[1])
            elif '*' in lhs:
                ans = multiply(lhs.split("*")[0],lhs.split("*")[1])
            elif '+' in lhs:
                ans = add(lhs.split("+")[0],lhs.split("+")[1])
            else:
                ans = minus(lhs.split("-")[0],lhs.split("-")[1])
        else:
            if '/' in rhs:
                if rhs.split('/')[0] == 'x':
                    ans =  multiply(lhs,rhs.split('/')[1])
                else:
                    ans = divide(rhs.split('/')[0],lhs)
            elif '*' in rhs:
                ans = divide(lhs, rhs.replace('x','').replace('*',''))
            elif '+' in rhs:
                ans = minus(lhs,rhs.replace('x','').replace('+',''))
            else:
                if rhs.split('-')[0] == 'x':
                    ans = add(rhs.split('-')[1],lhs)
                else:
                    ans = minus(rhs.split('-')[0],lhs)

    
    
    print("{:0.2f}".format(round_half_up(ans,2)))


