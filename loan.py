print("Please answer the following questions on a scale from 1-10, 10 being the biggest")
#Answer on a scale of 1-10, 10 being the biggest
loan = float(input("How large is the loan? "))
#Ask how large the loan is
credit = float(input("How good is your credit history? "))
#Ask how good their credit history is
income = float(input("How high is your income? "))
#Ask how high their income is
down_payment = float(input("How large is your down payment? "))
#Ask how large the down payment is

decision = False

if loan >= 5:
#If loan is at least 5
    if credit >= 7 and income >= 7:
    #If credit and income are at least 7
        decision = True
    elif credit >= 7 or income >= 7:
    #Else is credit of income are at least 7
        if down_payment >= 5:
        #If down payment is at least 5
            decision = True
        else:
        #Else (down payment is less than 5)
            decision = False
    else: 
    #Else (niether credit or income are at least 7)
        decision = False
else:
#Else (loan is less than 5)
    if credit < 4:
    #If credit is less than 4
        decision = False
    else:
    #Else (credit is at least 4)
        if income >= 7 or down_payment >= 7:
        #If income or down payment are at least 7
            decision = True
        elif income >= 4 and down_payment >= 4:
        #Else is income and down payment are at least 4
            decision = True
        else:
        #Else (income and down payment are both less than 4)
            decision = False

print("")
#Blank line

if decision:
    print("The decision is yes. This is a good loan.")
else:
    print("The decision is no. You should not loan this money.")

print("")
#Blank line