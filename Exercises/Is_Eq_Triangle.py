"""
1. Determine whether or not three input sides compose an equilateral triangle.
"""
print("Equilateral Triangle")

x = bool(0)
a = float(input("input 1 : "))
b = float(input("input 2 : "))
c = float(input("input 3 : "))

if((c==a)&(a==b)):
    x = 1
else:
    x = 0

print(bool(x))







