print("")
#Blank line
can_ride = False

age_one = float(input("What is the age of the first rider? "))
#How old is the first rider
height_one = float(input("What is the height (in inches) of the first rider? "))
#How tall is the first rider
second = input("Is there a second rider (yes/no)? ").lower()
#Is there a second rider

if second == 'yes':
    #If there is a second rider
    age_two = float(input("What is the age of the second rider? "))
    #How old is the second rider
    height_two = float(input("What is the height (in inches) of the second rider? "))
    #How tall is the second rider

if age_one >= 12 and age_one <= 17:
    #If the first rider is between 12 and 17 years old ask if they have a golden ticket
    golden_one = input("Does the first rider have a golden ticket (yes/no)? ").lower()
    if golden_one == 'yes':
        #If the first rider has a golden ticket set their age to 18 years old
        age_one = 18

if second == 'yes':
    #If there is a second rider
    if age_two >= 12 and age_two <= 17:
        #If the second rider is between 12 and 17 years old ask if they have a golden ticket
        golden_two = input("Does the second rider have a golden ticket (yes/no)? ").lower()
        if golden_two == 'yes':
            #If the second rider has a golden ticket set their age to 18 years old
            age_two = 18

if second == 'yes':
    #If there are two riders
    if height_one >= 36 and height_two >= 36:
        #Both must be at least 36 inches tall
        if age_one >= 18 or age_two >= 18:
            #And one must be at least 18 years old
            can_ride = True
        else:
            #If neuther rider is at least 18 years old
            if age_one >= 12 and age_two >= 12 and height_one >= 52 and height_two >= 52:
                #If both are at least 12 years old and 52 inches tall they can ride
                can_ride = True
            elif (age_one >= 16 or age_two >= 14) or (age_one >= 14 or age_two >= 16):
                #If one rider is at least 16 years old and the other is at least 14 years old they can ride
                can_ride = True
else:
    #If there is one rider
    if age_one >= 18 and height_one >= 62:
        #They must be at least 18 years old and 62 inches tall
        can_ride = True

print("")
#Blank line

if can_ride:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")

print("")
#Blank line