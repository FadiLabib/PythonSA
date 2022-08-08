#Fadi Labib
#11/15/2019
#All Rights Reservered
#Run Program

from prog01_useless_trivia import starbucks_addiction,kids,age_in_seconds,moon_weight,sun_weight
from prog01_useful_calc import menu,tip_calculator,car_sale,salary,quit

# Ask for the following inputs from the user remember to use the input function
# "Hi. What is your first name? "
first_name = ""
# "What is your last name? "
last_name = ""
# "How old are you? "
# REMEMBER your input needs to be in int; how do we cast an input to int
age = 0
# "Okay, last question. How many pounds do you weight? "
# REMEMBER your input needs to be in int; how do we cast an input to int
weight = 0;

##### DON"T MODIFY ANYTHING BELOW THIS LINE #####
print("\n\n\n***********************")
print("* Starbucks Addiction *")
print("***********************")
starbucks_addiction(first_name, last_name, age)

print("\n\n**************")
print("* Attention! *")
print("**************")
kids(first_name)

print("\n\n******************")
print("* Age in Seconds *")
print("******************")
age_in_seconds(age)

print("\n\n***************")
print("* Moon Weight *")
print("***************")
moon_weight(weight)

print("\n\n**************")
print("* Sun Weight *")
print("**************")
sun_weight(weight)


print("\nTHE END!\n\n")

# Menu to run through all the different userless calculation
# you pick what you like to calculate based on menu() options
# Based on you are promted for a certain input
option = None
while option != 0:
    menu()
    option = int(input("\nEnter number between 0 and 3: "))
    if round(option) == 1:
        resturant_bill_total = float(input("Enter Your Resturant Bill: "))
        tip_calculator(resturant_bill_total)
    elif round(option) == 2:
        car_price = float(input("Enter Your Car Price: "))
        car_sale(car_price)
    elif round(option) == 3:
        yearly_salary = float(input("Enter Your Yearly Salary: "))
        salary(yearly_salary)
    elif round(option) == 0:
        quit()
    else:
        print("\n\nYou have entered an invalid option!")
