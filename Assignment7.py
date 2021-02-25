"""Module #7 Assignment
Julie Haas
LIS 5937
Spring 2021"""

#1. Show current time
import sys
from datetime import datetime

print ("The current time is: ", datetime.today(), "\n")


#2. Add the timedelta to the datetime and subtract 60 seconds and add 2 years.
from datetime import timedelta

plus1day = datetime.today() + timedelta(days=1)
print("+ 1 day = ", plus1day)

minus60sec = plus1day - timedelta(seconds=60)
print("- 60 seconds = ", minus60sec)

plus2yrs = minus60sec + timedelta(days=730)
print("+ 2 years = ", plus2yrs)
print("\n")

#3. Create a timedelta object representing 100 days, 10 hours, and 13 minutes 
timeobj = timedelta(days=100) + timedelta(hours=10) + timedelta(minutes=13)
print("Timedelta object of 100 days, 10 hours, and 13 minutes: ")
print(timeobj,"\n")


#4. Write a function that takes two arguments (feet and inches) with this time object
def sound_calc(ft, inch):
    totalfeet = ft + (inch / 12)
    #speed of sound is 1,125 ft/s
    totalseconds = totalfeet/1125
    n = totalseconds

    days = n / (24 * 3600)
    hours = (n % (24*3600)) / 3600
    minutes = (n % 3600) / 60
    seconds = n % 60

    print("\nSound would take roughly\n {} day(s),\n {} hour(s),\n {} minute(s),\n and {} second(s)".
          format(round(days), round(hours), round(minutes), round(seconds,3)))
    print(" to travel over {} feet and {} inches.".format(ft, inch))
    print("If sent now, your sound parcel would arrive at", datetime.now() + timedelta(seconds = totalseconds))
   

def main():
    print("Please enter separate values for feet and inches:")
    feet = int(input(" Feet: "))
    inches = int(input(" Inches: "))
    sound_calc(feet,inches)

main()
