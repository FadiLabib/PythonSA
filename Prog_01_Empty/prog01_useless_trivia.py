# Useless Trivia Program
DAYS_PER_YEAR = 365.2422
HOURS_PER_DAY = 24
MIN_PER_HOUR = 60
SEC_PER_MIN = 60
REBEAT = 5
MOON_MULT = 6
SUN_MULT = 27.1

# Calculates the number of Starbucks drinks since your birth
# Recieves first and last name along with age
# Prints the number of Starbucks drinks you had since your birth
def starbucks_addiction(first, last, age):
    # Convert first to be in upper case; What function should you use?
    first_name_upper = first.upper()
    # Convert first to be in lower case; What function should you use?
    first_name_lower = first.lower()
    # Calculate rounded number of drinks to nearest whole number
    # This can be done by multiplying age by DAYS_PER_YEAR
    # Remember to use the round() function
    rounded_drinks = round(age*DAYS_PER_YEAR)
    # Calculate the acutal number of cups without rounding
    drinks = age*DAYS_PER_YEAR
    print("Hello,",first+" "+last+"!","Did you know," \
            + " if you go to Starbucks everyday, since you were born," \
            + " you would have had about",rounded_drinks,"drinks")
    print("Now,",first_name_upper+",","If you want to be really accurate," \
            + " that is exactly",drinks,"drinks")
    print("I will calm down,",first_name_lower+",","it doesn't matter, " \
            + "you have a serious addiction problem!\n")

# Think how kids would call your name if they want to get your attention
# Recieves first name 
# Prints first name repeating it REBEAT number of times
def kids(first):
    first_name = first+" "
    # think how you will make first name print REBEAT number of times
    called = ""
    print("If a small child were trying to get your attention,")
    print("your name would become: ")
    print(called)

# Calculate your age in seconds
# Recieves age
# Prints age in seconds
def age_in_seconds(age):
    # Think how you can use globals defined above to find # of seconds
    seconds = 0
    print("You're over", round(seconds), "seconds old.")

# Calculate your moon weight
# Recieves weight
# Prints your weight on the moon
def moon_weight(weight):
    # moon weight is weight divided by MOON_MULT
    moon_weight = 0.00
    print("Did you know that on the moon you would weigh only",moon_weight,"pounds?")

# Calculate your sun weight
# Recieves weight
# Prints your weight on the sun, if you are lucky
def sun_weight(weight):
    # sun weight is weight multiplied by SUN_MULT
    sun_weight = 0.00
    print("On the sun, you'd weigh",sun_weight,"(but, ah... not for long).")
