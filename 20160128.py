balance = 39260
annualInterestRate = 0.2
monthlyPayment = 0
newBalance = 0

newBalance = balance
while newBalance > 0:
    newBalance = balance
    monthlyPayment += 10
    month = 1
    while month <= 12 and newBalance > 0:
        newBalance -= monthlyPayment
        newBalance *= (annualInterestRate/12 + 1)
        month += 1
    newBalance = round(newBalance,2)
print("Lowest Payment: "+str(monthlyPayment))
