child_meal = float(input("What is the price of a child's meal? $"))
#Ask for price of child's meal
child_drink = float(input("What is the price of a child's drink? $"))
#Ask for price of child's drink
child_app = float(input("What is the price of a child's appetizer? $"))
#Ask for price of child's appetizer
adult_meal = float(input("What is the price of an adult's meal? $"))
#Ask for price of adult's meal
adult_drink = float(input("What is the price of a adult's drink? $"))
#Ask for price of adult's drink
adult_app = float(input("What is the price of a adult's appetizer? $"))
#Ask for price of adult's appetizer
child_number_meal = int(input("How many children are getting a meal? "))
#Ask how many children are getting a meal
child_number_drink = int(input("How many children are getting a drink? "))
#Ask how many children are getting a drink
child_number_app = int(input("How many children are getting a appetizer? "))
#Ask how many children are getting a appetizer
adult_number_meal = float(input("How many adults are getting a meal? "))
#Ask how many adults are getting a meal
adult_number_drink = float(input("How many adults are getting a drink? "))
#Ask how many adults are getting a drink
adult_number_app = float(input("How many adults are getting a appetizer? "))
#Ask how many adults are getting a appetizer
sales_tax = float(input("What is the sales tax rate? "))
#Ask for sales tax amount

print("")
#Blank line

child_meal_total = float(child_meal * child_number_meal)
#Calculate children's meal total
child_drink_total = float(child_drink * child_number_drink)
#Calculate children's drink total
child_app_total = float(child_app * child_number_app)
#Calculate children's appetizer total
child_subtotal = float(child_meal_total + child_drink_total + child_app_total)
#Calculate children's subtotal
adult_meal_total = float(adult_meal * adult_number_meal)
#Calculate adult's meal total
adult_drink_total = float(adult_drink * adult_number_drink)
#Calculate adult's drink total
adult_app_total = float(adult_app * adult_number_app)
#Calculate adult's appetizer total
adult_subtotal = float(adult_meal_total + adult_drink_total + adult_app_total)
#Calculate adult's subtotal
subtotal = float(child_subtotal + adult_subtotal)
#Calculate subtotal
print("Subtotal: $" + str(subtotal))
#Print subtotal
sales_tax_decimal = float(sales_tax / 100)
#Make tax rate a decimal
sales_tax_amount = float(subtotal * sales_tax_decimal)
#Calculate sales tax
rounded_tax = f"{sales_tax_amount:.2f}"
#Round salex tax
print("Sales Tax: $" + str(rounded_tax))
#Print sales tax amount
total = float(subtotal + sales_tax_amount)
#Calculate total
rounded_total = f"{total:.2f}"
#Round total
print("Total: $" + str(rounded_total))
#Print total

print("")
#Blank line

payment = float(input("What is the payment amount? $"))
#Ask for payment amount
change = float(payment - total)
#Calculate change
rounded_change = f"{change:.2f}"
#Round change
print("Change: $" + str(rounded_change))
#Print change

print("")
#Blank line