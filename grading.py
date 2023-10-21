grade = float(input("What is your percentage grade? "))
#Ask for percentage grade
if grade >= 90:
    letter = "A"
    #If grade is at least 90 set letter to A
elif grade >= 80:
    letter = "B"
    #If grade is at least 80 set letter to B
elif grade >= 70:
    letter = "C"
    #If grade is at least 70 set letter to C
elif grade >= 60:
    letter = "D"
    #If grade is at least 60 set letter to D
else:
    letter = "F"
    #If grade is less than 60 set letter to F
if grade % 10 >= 7:
    extra = "+"
    #If grade divided by ten has a remainder of at least 7 set extra to +
elif grade % 10 >= 3:
    extra = ""
    #If grade divided by ten has a remainder of at least 3 set extra to nothing
else:
    extra = "-"
    #If grade divided by ten has a remainder of less than 3 set extra to -
if grade >= 93:
    extra = ""
    #If grade is over 93 set extra to nothing
if grade < 60:
    extra = ""
    #If grade is less than 60 set extra to nothing
print("Your letter grade is a " + letter + extra)
#Print letter grade with extra
if grade >= 70:
    print("Congradulations! You passed the class!")
    #If grade is at least 70 they passed
else:
    print("Unfortunatley, you failed the class")
    #If grade is less than 70 they failed