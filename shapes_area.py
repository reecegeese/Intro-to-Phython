square_length = float(input("What is the length of a side of the square? "))
#Ask for a side
square_area = str(square_length * square_length)
#Calculate area
print("The area of the square is: " + square_area)
#Print square's area
rectangle_length = float(input("What is the length of the rectangle? "))
#Ask for rectangle length
rectangle_width = float(input("What is the width of the rectangle? "))
#Ask for rectangle width
rectangle_area = str(rectangle_length * rectangle_width)
#Calculate rectangle area
print("The area of the rectangle is: " + rectangle_area)
#Print rectangle's area
circle_radius = float(input("What is the radius of the circle? "))
#Ask for radius of the circle
radius_squared = float(circle_radius ** 2)
#Square the radius
circle_area = str(3.14 * radius_squared)
#Calculate area of the circle
print("The area of the circle is: " + circle_area)