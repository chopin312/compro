"""
0. Determine whether or not three input sides compose a right triangle.
"""
x = bool(0)
a = float(input())
b = float(input())
c = float(input())

if (c >= a) & (c >= b) & (c ** 2 == a ** 2 + b ** 2):
    x = 1
elif (a >= b) & (a >= c) & (c ** 2 + b ** 2 == a ** 2):
    x = 1
elif (b >= a) & (b >= c) & (c ** 2 + a ** 2 == b ** 2):
    x = 1
else:
    x = 0

print(bool(x))







