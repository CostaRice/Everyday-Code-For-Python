monthlyPayment = 0
annualInterestRate = 0.2
balance = 4773
monthlyInterestRate = annualInterestRate / 12.0

newBalance = balance - 10
while newBalance > 0:
    monthlyPayment += 10
    newBalance = balance
    month = 0
    while month < 12 and newBalance > 0:
        newBalance -= monthlyPayment
        newBalance *= monthlyInterestRate+1
        month += 1
    newBalance = round(newBalance,2)
print " Lowest Payment:", monthlyPayment
