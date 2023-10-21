import math
print("Welcome to the velocity calculator. Please enter the following: ")

print("")
#blank line

mass = float(input("Mass (in kg): "))
#Ask for mass
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
#Ask for gravity
time = float(input("Time (in seconds): "))
#Ask for time
density = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
#Ask for density
area = float(input("Cross sectional area (in m^2): "))
#Ask for area
drag = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))
#Ask for drag
c = (1 / 2) * density * area * drag
#Calculate c
velocity = math.sqrt(mass * gravity / c) * (1 - math.exp((-math.sqrt(mass * gravity * c) / mass) * time))
#Calculate velocity

print("")
#blank line

print("The inner value of c is: " + str(f"{c:.3f}"))
print("The velocity after " + str(time) + " seconds is: " + str(f"{velocity:.3f}") + (" m/s")) 