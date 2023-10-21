print("")
#Blank line

ask_age = input("How old are you? ")
#Ask for age
age = int(ask_age)
#Make age a interger
next_age = age + 1
#Add one to age
next_age_string = str(next_age)
#Makes next_age a string so it can be printed
print(f"On your next birthday, you will be " + next_age_string)
#Print age + 1

print("")
#Blank line

ask_cartons = input("How many egg cartons do you have? ")
#Ask how many egg cartons
cartons = int(ask_cartons)
#Make ask_cartons a interger
eggs = cartons * 12
#Divide by 12
eggs_string = str(eggs)
#Make eggs a string
print("You have " + eggs_string + " eggs")
#Print how many eggs you have

print("")
#Blank line

ask_cookies = input("How many cookies do you have? ")
#Ask how many cookies
ask_people = input("How many people are there? ")
#Ask how many people there are
cookies = int(ask_cookies)
people = int(ask_people)
#Turns both into intergers
cookies_per_person = cookies / people
#Calculates how many cookies each peron should get
cookies_per_person_string = str(cookies_per_person)
#Turns how many cookies each person may have into a string
print("Each person may have " + cookies_per_person_string + " cookies")
#Prints how many cookies each person may have

print("")
#Blank line