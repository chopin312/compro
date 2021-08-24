"""
4. Shifts the bits in an input string one place to the right. The rightmost bit wraps around to the leftmost position.
"""
x = input()
z = x[-1] + x[0: -1]
print(z)
