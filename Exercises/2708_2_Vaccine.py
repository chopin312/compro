# gather input
Infected = input("Had you infected? (y or n) :")
Vaccine = input("Had you vaccinated? (y or n) :")
if Vaccine == "y":
    NumDose = int(input("How many dose did you get? :"))
    print("Input \nsv for Sinovac \naz for AstraZeneca\nsp for SinoPharm")
    Vacc = [0, 0, 0, 0]
    i = 1
    while i <= NumDose:
        Vacc[i] = input("What is your Dose%d ? :" % i)
        if Vacc[i] == "sv" or Vacc[i] == "az" or "sp" == Vacc[i]:
            i += 1
        else:
            print("Invalid input plz input again", i)
# conditions
Pfizer = int(0)
if Vaccine == "n":
    if Infected == "n":
        Pfizer = 2
    else:
        Pfizer = 1
else:
    if NumDose == 1:
        Pfizer = 1
    elif NumDose == 2:
        if Vacc[1] == Vacc[2] == "sv" or Vacc[1] == Vacc[2] == "sp":
            Pfizer = 1
print("you will get", Pfizer, "dose(s) of Pfizer")
