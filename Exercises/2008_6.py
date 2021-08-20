"""
6. Compute a person's income tax.
    a. Significant constants
        i. tax rate
        ii. standard deduction
        iii. deduction per dependent
    b. The inputs are
        i. gross income
        ii. number of dependents
    c. Computations:
        i. net income = gross income - the standard deduction - a deduction for each dependent
        ii. income tax = is a fixed percentage of the net income
    d. The outputs are
    i. the income tax, rounded to two figures
"""
# Significant constants
tax_rate = 0.2
standard_deduction = 10000
deduction_per_dependent = 3000
# The inputs are
gross_income = float(input("Gross income : "))
number_of_dependents = float(input("number of dependents : "))
# Computations
net_income = gross_income - standard_deduction - (deduction_per_dependent * number_of_dependents)
income_tax = net_income * tax_rate
print("Your income before tax is", net_income)
print("Your income tax is", round(income_tax, 2))
print("Your income after tax is", net_income - income_tax)