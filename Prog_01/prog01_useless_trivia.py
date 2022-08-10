# Useless Trivia Program
DAYS_PER_YEAR = 365.2422
HOURS_PER_DAY = 24
MIN_PER_HOUR = 60
SEC_PER_MIN = 60
REBEAT = 5
MOON_MULT = 6
SUN_MULT = 27.1


def starbucks_addiction(first, last, age):
    first_name_upper = first.upper()
    first_name_lower = first.lower()
    print("Hello,",first+" "+last+"!","Did you know," \
            + " if you go to Starbucks everyday, since you were born," \
            + " you would have had about",round(age*DAYS_PER_YEAR),"drinks")
    print("Now,",first_name_upper+",","If you want to be really accurate," \
            + " that is exactly", age*DAYS_PER_YEAR,"drinks")
    print("I will calm down,",first_name_lower+",","it doesn't matter, " \
            + "you have a serious addiction problem!\n")

def kids(first):
    first_name = first+" "
    called = first_name*REBEAT
    print("If a small child were trying to get your attention,")
    print("your name would become: ")
    print(called)

def age_in_seconds(age):
    seconds = age*DAYS_PER_YEAR*HOURS_PER_DAY*MIN_PER_HOUR*SEC_PER_MIN
    print("You're over", round(seconds), "seconds old.")

def moon_weight(weight):
    moon_weight = weight/MOON_MULT
    print("Did you know that on the moon you would weigh only",moon_weight,"pounds?")

def sun_weight(weight):
    sun_weight = weight*SUN_MULT
    print("On the sun, you'd weigh",sun_weight,"(but, ah... not for long).")
