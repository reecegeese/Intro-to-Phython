temp_fahr = float(input("What is the temperature in Fahrenheit? "))
#Ask for temprature in Fahrenheit
farh32 = float(temp_fahr - 32)
#Subtract 32 from the Farhenhiet temperature
fraction = float(5/9)
#Define the fraction 5/9
fahr_cel = float(farh32 * fraction)
#Multiply the subracted temperature by 5/9
print(f"The temperature in Celsius is " + str(float(f"{fahr_cel:.1f}")))
#Print the new temperature in Celsius

print("")
#Blank line

temp_cel = float(input("What is the temperature in Celcius? "))
#Ask for the temperature in Celsius
cel_fraction = float(temp_cel / fraction)
#Divide the temperature in Celcius by the fraction 5/9
cel_32 = float(cel_fraction + 32)
#Add 32 to the dividend
print(f"The temperature in Fahrenheit is " + str(float(f"{cel_32:.1f}")))
#Print the new temperature in Fahrenheit