"""
1. Determine whether or not three input sides compose an equilateral triangle.
"""
x = bool(0)
a = float(input())
b = float(input())
c = float(input())

if((c==a)&(a==b)):
    x = 1
else:
    x = 0

print(bool(x))







