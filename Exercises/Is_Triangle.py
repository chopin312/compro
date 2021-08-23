"""
0. Determine whether or not three input sides compose a triangle.
"""
print("Triangle")

x = bool(0)
a = float(input("input 1 : "))
b = float(input("input 2 : "))
c = float(input("input 3 : "))

if((c>=a)&(c>=b)&(a+b>c)):
    x = 1
elif((a>=b)&(a>=c)&(c+b>a)):
    x = 1
elif((b>=a)&(b>=c)&(c+a>b)):
    x = 1
else:
    x = 0

print(bool(x))







