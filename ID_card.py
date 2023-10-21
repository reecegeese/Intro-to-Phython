print("Please enter the following information")

first = input("First name: ").capitalize()
#Ask for first name
last = input("Last name: ").capitalize()
#Ask for last name
email = input("Email address: ")
#Ask for email address
phone = input("Phone number: ")
#Ask for phone number
job = input("Job title: ").title()
#Ask for job title
id = input("ID number: ")
#Ask for ID number
hair = input("Hair color: ").capitalize()
#Ask for hair color
eye = input("Eye color: ").capitalize()
#Ask for eye color
month = input("Month started: ").capitalize()
#Ask for month started
training = input("Have you completed advanced training: ").capitalize()
#Ask if they have completed advanced training

print("")
#Blank line

print("The ID card is: ")
print("----------------------------------------")
print(last.upper() + ", " + first)
#Print LAST, First
print(job)
#Print Job Title
print("ID: " + id)
#Print ID Number

print("")
#Blank line

print(email.lower())
#Print email
print(phone)
#Print phone number

print("")
#Blank line

print("Hair: %-*s   Eyes: %s" % (10, hair, eye))
#Print Hair: Color       Eyes: Color
print("Month: %-*s  Training: %s" % (10, month, training))
#Print Month: Month      Training: Yes or No
print("----------------------------------------")

print("")
#Blank line