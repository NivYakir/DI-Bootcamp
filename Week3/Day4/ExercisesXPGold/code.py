import holidays
import datetime

# Exercise 1: Upcoming Holiday

uk_holidays = holidays.UnitedKingdom()

def today_date():
    today = datetime.date.today()

    for i in range(1, 365):
        future_date = today + datetime.timedelta(days=i)
        if future_date in uk_holidays:
            print(f"The next U.K. holiday is on {future_date}: {uk_holidays[future_date]}")
            break

# Exercise 2: How Old Are You on Jupiter?

planets = {'Mercury' : 0.2408467, 'Venus' : 0.61519726, 'Earth' : 1, 
           'Mars' : 1.8808158, 'Jupiter' : 11.862615, 'Saturn' : 29.447498,
           'Uranus' : 84.016846, 'Neptune' : 164.79132}

def planet_age(age, planet):
    planet_year_in_days = datetime.timedelta(days=365.25 * planets[planet])
    age_on_planet = round(age / planet_year_in_days.total_seconds(), 2)
    print(age_on_planet)

planet_age(1000000000,'Neptune')

