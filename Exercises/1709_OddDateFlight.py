Year = [31,28,31,30,31,30,31,31,30,31,30,31]
Nok = 0
for Mount in Year:
    for Day in range(1, Mount+1):
        if Day % 2 == 1:
            Nok +=1
print(Nok)
