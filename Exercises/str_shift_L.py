"""
3. Shifts the bits in an input string one place to the left. The leftmost bit wraps around to the rightmost position.
"""
x = input()
z = x[1: -1] + x[-1] + x[0]
print(z)
