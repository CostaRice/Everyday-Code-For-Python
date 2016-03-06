print 'Please think of a number between 0 and 100!'

high = 100
low = 0
result = False
while not result:
    answer = (high+low)/2
    print 'Is your secret number '+str(answer)+'?'
    user_input = str(raw_input("Enter 'h' to indicate the guess is too high. "
                               "Enter 'l' to indicate the guess is too low. "
                               "Enter 'c' to indicate I guessed correctly."))
    if user_input == 'h':
        high = answer
    elif user_input == 'l':
        low = answer
    elif user_input == 'c':
        result = True
        print("Game over. Your secret number was: "+str(answer))
    else:
        print "Sorry, I did not understand your input."
