"""
Simple Calculator + - * / %
"""

FirstInput = float(input("Input first number : "))
SecondInput = float(input("Input second number : "))
Operator = input("Input your operator : ")

if(Operator == '+'):
    print(FirstInput + SecondInput)
elif(Operator == '-'):
    print(FirstInput - SecondInput)
elif(Operator == '*'):
    print(FirstInput * SecondInput)
elif(Operator == '/'):
    print(FirstInput / SecondInput)
elif(Operator == '%'):
    print(FirstInput % SecondInput)
else:
    print("ERROR")

