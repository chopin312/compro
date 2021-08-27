x = float(input("Input your score : "))

if 80 <= x <= 100:
    print("A")
elif x >= 75:
    print("B+")
elif x >= 70:
    print("B")
elif x >= 65:
    print("C+")
elif x >= 60:
    print("C")
elif x >= 55:
    print("D+")
elif x >= 50:
    print("D")
else:
    print("F")
