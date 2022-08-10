#Useful Calc Program

# Displays avilable options for this program
def menu():
    print("\nWhat would you like to Calculate? ")
    print("0: Quit")
    print("1: Tip Calculator")
    print("2: Car Salesman")
    print("3: Salary Calculator")

# Calculates percentage
# Recieves a percent and a whole amount
# Returns a percentage
def percentage(percent, whole):
    # calculate percentage 
    percentage = float(percent)*float(whole)/100
    return percentage

# Calculates 15% and 20% Tips
# Recieve the bill before applying tip
# Prints results
def tip_calculator(total_bill):
    print("\nWelcome to Tip Calculator")
    # calculate 15% tip using percentage function from above
    fifteen_perc_tip = percentage(15, total_bill)
    # calculate 20% tip using percentage function from above
    twenty_perc_tip = percentage(20, total_bill)
    # calculate total bill original bill + 15% tip
    bill_plus_15 = total_bill + fifteen_perc_tip
    # calculate total bill origianl bill + 20% tip
    bill_plus_20 = total_bill + twenty_perc_tip
    # display calculation results
    print("If your total bill is $"+str(total_bill),"then: ")
    print("15% Tip is: $"+str(fifteen_perc_tip))
    print("Total Bill is: $"+str(bill_plus_15))
    print("20% Tip is: $"+str(twenty_perc_tip))
    print("Total Bill is: $"+str(bill_plus_20)) 

# Calculates the new price for a car after adding additional costs
# Recieves the original car price
# prints original car cost and cost after additional fees are added
def car_sale(car_price):
    print("\nWelcome to Car Sales Program")
    # calculate taxes as 4.5% of original car price
    taxes = 0.00
    # calculate license as 1.4% of original car price
    license = 0.00
    # set dealers_prep to 250.00
    dealers_prep = 0.00
    # set insurance to 4000.00
    insurance = 0.00
    # calculate total price after adding taxes, licnese, dealer_prep, and insurance
    total_price = 0.00
    print("\nIf you buy a car that costs $"+str(car_price),"then " \
            + "you would be paying: $"+str(total_price))

# Converts a yearly salary to different rates
# Recieves yearly salary
# Prints the results in differnt rates
def salary(yearly_salary):
    print("\nWelcome to Salary Calculator!")
    # Taking two weeks of unpaid vacation time.
    # Working 50 weeks per year at 40 hrs per week = 2000 hours
    # Find the hourly salary and use the round function rounding to two decimal places
    two_wks_unpaid_vac = 0
    # Find the daily rate by multiplying two_wks_unpaid_vac by 8
    two_wks_unpaid_vac_daily = 0
    print("\n\nTwo Weeks Unpaid Vacations: ")
    print("Your Hourly Rate is:$"+str(two_wks_unpaid_vac)+" hourly or $"+str(two_wks_unpaid_vac_daily)+" daily")
    #Taking two weeks of paid vacation time or taking no vacations
    #Working 52 weeks per year at 40 hrs per week = 2080 hours
    # Find the hourly salary and use the round function to two decimal places
    two_wks_paid_vac = 0
    # Find the daily salary just like you did before
    two_wks_paid_vac_daily = 0
    # Use two print statements similar to the two weeks unpaid vacation example to display results
    print("Something...")
    print("SOmething...")

    # 2019 Holiday Schedules 
    # Taking 6 holidays = 255 days to Taking 14 holidays = 247 days
    initial_holidays = 6
    print("\n\nHourly Rate Based On 2019 Holidays Count: ")
    for i in range(255,246,-1):
        hourly_rate = round(yearly_salary/(i*8), 2)
        daily_rate = round(hourly_rate*8, 2)
        print(initial_holidays," holidays =>", i, "days => $"+str(hourly_rate)+" per hour or $"+str(daily_rate)+" daily")
        initial_holidays += 1
    # Monthly Payment assuming bi-weekly paycheck
    # Think of it that a year has 13 4-weeks periods
    # Use round function to two decimal place and the yearly salary and the number of weeks to calculate monthly salary
    monthly_salary_bi_week = 0
    # Think of it that a year has 26 2-weeks periods
    # Use round function to two decimal places and the yearly salary and the number of weeks to calculate bi weekly salary
    bi_weekly_salary = 0
    # Weekly Payment assuming 52 Weeks per Year
    # use the round function to two decimal place and the yearly salary and the number of weeks to calculate weekly salary
    weekly_salary = 0
    # Printing the different results
    print("\n\nMonthly Salary Assuming Bi-Weekly Checks: $"+str(monthly_salary_bi_week))
    print("Your Bi-Weekly Salary Is: $"+str(bi_weekly_salary))
    print("Weekly Salary Based on 52 Weeks Year: $"+str(weekly_salary))

# Displays a Message and quits the program
def quit():
    print("\nThank you for using our calculator service!")
