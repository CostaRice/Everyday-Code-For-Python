balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyPayment = 0
totalPayment = 0
interest = 0
count = 1
while count <= 12:
    monthlyPayment = balance * monthlyPaymentRate
    totalPayment += monthlyPayment
    balance -= monthlyPayment
    balance *= (annualInterestRate/12.0+1)
    print ("Month: "+str(count))
    print ("Minimum monthly payment: "+str(round(monthlyPayment, 2)))
    print("Remaining balance: "+str(round(balance,2)))
    count += 1
print("Total paid: "+str(round(totalPayment, 2)))
print ("Remaining balance: "+str(round(balance, 2)))




