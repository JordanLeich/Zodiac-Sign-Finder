# Created by Diana Balderas and Jordan Leich, Original release: 5/17/2020, Updated on 7/8/2020.
# Email jordanleich@gmail.com if you wish to collaborate or work together sometime.
# Instructions: Enter you birth month in lowercase letters and enter your birth date in numbers.

# Imports
import time
import restart


# Main zodiac code finder
def start():
    user_month = str(input('In what month were you born? '))
    print()
    time.sleep(1)
    user_date = int(input('What day were you born? '))
    print()
    time.sleep(1)

    if user_date < 1:  # Used when a user sets a birth date lower than 1
        print("Invalid birth date provided!\n")
        time.sleep(2)
        restart.restart()

    elif user_date > 31:  # Used when a user sets a birth date higher than 31
        print("Error found! Your birth date is too high!\n")
        time.sleep(2)
        restart.restart()

    months = [
        'january',
        'february',
        'march',
        'april',
        'june',
        'july',
        'august',
        'september',
        'november',
        'december',
    ]

    if user_month.lower() in months:

        if user_month.lower() == 'december':
            user_sign = ('sagittarius' if user_date < 22 else 'capricorn')
            results(user_sign)
        elif user_month.lower() == 'january':
            user_sign = ('capricorn' if user_date < 20 else 'aquarius')
            results(user_sign)
        elif user_month.lower() == 'february':
            user_sign = ('aquarius' if user_date < 19 else 'pisces')
            results(user_sign)
        elif user_month.lower() == 'march':
            user_sign = ('pisces' if user_date < 21 else 'aries')
            results(user_sign)
        elif user_month.lower() == 'april':
            user_sign = ('aries' if user_date < 20 else 'taurus')
            results(user_sign)
        elif user_month.lower() == 'may':
            user_sign = ('taurus' if user_date < 21 else 'gemini')
            results(user_sign)
        elif user_month.lower() == 'june':
            user_sign = ('gemini' if user_date < 21 else 'cancer')
            results(user_sign)
        elif user_month.lower() == 'july':
            user_sign = ('cancer' if user_date < 23 else 'leo')
            results(user_sign)
        elif user_month.lower() == 'august':
            user_sign = ('leo' if user_date < 23 else 'virgo')
            results(user_sign)
        elif user_month.lower() == 'september':
            user_sign = ('virgo' if user_date < 23 else 'libra')
            results(user_sign)
        elif user_month.lower() == 'october':
            user_sign = ('libra' if user_date < 23 else 'scorpio')
            results(user_sign)
        elif user_month.lower() == 'november':
            user_sign = ('scorpio' if user_date < 22 else 'sagittarius')
            results(user_sign)

    else:  # Used if the users birth month is not recognized or found
        print("Error found!\n")
        time.sleep(2)
        restart.restart()


def results(user_sign):
    time.sleep(1)
    print('Your zodiac sign is a ' + user_sign + '!\n')
    time.sleep(2)
    restart.restart()


start()
