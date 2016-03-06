balance = 320000
annualInterestRate = 0.2

monthlyPayment = 0
newBalance = 0

monthlyPayment_low = balance/12.0
monthlyPayment_high = (balance * (1 + annualInterestRate/12.0)**12)/12.0

newBalance = balance
while abs(newBalance) > 0.01:
    newBalance = balance
    monthlyPayment = (monthlyPayment_high+monthlyPayment_low)/2.0
    month = 1
    while month <= 12:
        newBalance -= monthlyPayment
        newBalance *= (annualInterestRate/12.0 + 1)
        month += 1
    if newBalance > 0:
        monthlyPayment_low = monthlyPayment
    elif newBalance < 0:
        if newBalance > -0.01:
            break
        else:
            monthlyPayment_high = monthlyPayment

print("Lowest Payment: "+str(round(monthlyPayment, 2)))
