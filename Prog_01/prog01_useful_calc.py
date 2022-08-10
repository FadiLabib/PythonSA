#Useful Calc Program

def menu():
    print("\nWhat would you like to Calculate? ")
    print("0: Quit")
    print("1: Tip Calculator")
    print("2: Car Salesman")
    print("3: Salary Calculator")

def percentage(percent, whole):
    return (float(percent)*float(whole))/100

def tip_calculator(total_bill):
    print("\nWelcome to Tip Calculator")
    fifteen_perc_tip = percentage(total_bill, 15)
    twenty_perc_tip = percentage(total_bill, 20)
    bill_plus_15 = total_bill+fifteen_perc_tip
    bill_plus_20 = total_bill+twenty_perc_tip
    print("If your total bill is $"+str(total_bill),"then: ")
    print("15% Tip is: $"+str(fifteen_perc_tip))
    print("Total Bill is: $"+str(bill_plus_15))
    print("20% Tip is: $"+str(twenty_perc_tip))
    print("Total Bill is: $"+str(bill_plus_20)) 

def car_sale(car_price):
    print("\nWelcome to Car Sales Program")
    taxes = percentage(car_price, 4.5)
    license = percentage(car_price, 1.4)
    dealers_prep = 250.00
    insurance = 4000.00
    total_price = car_price+taxes+license+dealers_prep+insurance
    print("\nIf you buy a car that costs $"+str(car_price),"then " \
            + "you would be paying: $"+str(total_price))

def salary(yearly_salary):
    print("\nWelcome to Salary Calculator!")
    #Taking two weeks of unpaid vacation time.
    #Working 50 weeks per year at 40 hrs per week = 2000 hours
    two_wks_unpaid_vac = round(yearly_salary/2000, 2)
    two_wks_unpaid_vac_daily = two_wks_unpaid_vac*8
    print("\n\nTwo Weeks Unpaid Vacations: ")
    print("Your Hourly Rate is:$"+str(two_wks_unpaid_vac)+" hourly or $"+str(two_wks_unpaid_vac_daily)+" daily")
    #Taking two weeks of paid vacation time or taking no vacations
    #Working 52 weeks per year at 40 hrs per week = 2080 hours
    two_wks_paid_vac = round(yearly_salary/2080, 2)
    two_wks_paid_vac_daily = two_wks_paid_vac*8
    print("\n\nTwo Weeks of Paid Vacations: ")
    print("Your Hourly Rate is:",two_wks_paid_vac,"hourly or $"+str(two_wks_paid_vac_daily)+" daily")
    
    #2019 Holiday Schedules 
    #Taking 6 holidays = 255 days to Taking 14 holidays = 247 days
    initial_holidays = 6
    print("\n\nHourly Rate Based On 2019 Holidays Count: ")
    for i in range(255,246,-1):
        hourly_rate = round(yearly_salary/(i*8), 2)
        daily_rate = round(hourly_rate*8, 2)
        print(initial_holidays," holidays =>", i, "days => $"+str(hourly_rate)+" per hour or $"+str(daily_rate)+" daily")
        initial_holidays += 1
    #Monthly Payment assuming bi-weekly paycheck
    #Think of it that a year has 13 4-weeks periods
    #Think of it that a year has 26 2-weeks periods
    #Weekly Payment assuming 52 Weeks per Year
    monthly_salary_bi_week = round(yearly_salary/13, 2)
    bi_weekly_salary = round(yearly_salary/26, 2)
    weekly_salary = round(yearly_salary/52, 2)
    print("\n\nMonthly Salary Assuming Bi-Weekly Checks: $"+str(monthly_salary_bi_week))
    print("Your Bi-Weekly Salary Is: $"+str(bi_weekly_salary))
    print("Weekly Salary Based on 52 Weeks Year: $"+str(weekly_salary))

def quit():
    print("\nThank you for using our calculator service!")
