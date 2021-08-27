"""
1. The computer guesses the user's number using the minimum number of attempts and prevents cheating by the user.
"""

Min = int(input("Input Minimum Number : "))
Max = int(input("Input Maximum Number : "))

Count = 1
# Guess = int((Max + Min)/2)
Check = "0"

while 1:
    Guess = int((Max + Min) / 2)
    print("I guess it : " + str(Guess))
    Check = input("Is it > , < , = : ")
    if Check == ">":
        if Guess == Max - 1:
            print("The answer is", str(Max), "I guess it in", str(Count + 1), "try(s)")
            break
        Min = Guess
    elif Check == "<":
        if Guess == Min + 1:
            print("The answer is", str(Min), "I guess it in", str(Count + 1), "try(s)")
            break
        Max = Guess
    elif Check == "=":
        print("The answer is", str(Guess), "I guess it in", str(Count), "try(s)")
        break
    Count += 1
