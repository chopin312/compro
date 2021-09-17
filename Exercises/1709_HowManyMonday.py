Day = 365
FirstDay = 6
InterDay = 2

Count = 0
D = FirstDay
for i in range(1, Day+1):
    print(D)
    if D == InterDay:
        Count += 1
    if D == 7:
        D = 1
    else:
        D += 1

print(Count)

