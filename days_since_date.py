# Imports
import datetime

# Get start date
current_date = datetime.datetime.now().strftime("%d") + "/" + datetime.datetime.now().strftime("%m") + "/" + datetime.datetime.now().strftime("%Y")
print(f"Dates should follow DD/MM/YYYY format e.g. {current_date}")

while 1:
    try:
        # DD/MM/YYYY
        date = str(input("Date: "))
        date = date.split("/")

        # Enforces that months be between 1 and 12 inclusive and years be from 0 AD up until the current year
        assert int(date[1]) <= 12 and int(date[1]) > 00 and int(date[2]) <= int(datetime.datetime.now().strftime("%Y")) and int(date[2]) >= 0000

        # Enforces that days is actually possible within given month
        assert int(date[0]) > 00

        ## Months with 31 days
        if int(date[1]) == 1 or int(date[1]) == 3 or int(date[1]) == 5 or int(date[1]) == 7 or int(date[1]) == 8 or int(date[1]) == 10 or int(date[1]) == 12:
            assert int(date[0]) <= 31
        ## Months with 30 days
        elif int(date[1]) == 4 or int(date[1]) == 6 or int(date[1]) == 9 or int(date[1]) == 11:
            assert int(date[0]) <= 30
        ## February
        else:
            if int(date[2]) % 4 != 0:
                assert int(date[0]) <= 28
            elif int(date[2]) % 100 != 0:
                assert int(date[0]) <= 29
            elif int(date[2]) % 400 != 0:
                assert int(date[0]) <= 28
            else:
                assert int(date[0]) <= 29

        # Ensure that date has not already passed
        if int(date[2]) == int(datetime.datetime.now().strftime("%Y")):
            assert int(date[1]) <= int(datetime.datetime.now().strftime("%m"))

        if int(date[1]) == int(datetime.datetime.now().strftime("%m")):
            assert int(date[0]) <= int(datetime.datetime.now().strftime("%d"))

        break
    except:
        print("Invalid input: dates should be formatted DD/MM/YYYY")

# Calculate how long ago that was

## Calculate days from years
years_ago = int(datetime.datetime.now().strftime("%Y")) - int(date[2])

### Calculate leap days
days = 0
for i in range(int(date[2]), int(datetime.datetime.now().strftime("%Y")) + 1):
    if int(datetime.datetime.now().strftime("%m")) > 2 or i != int(datetime.datime.now().strftime("%Y")): # verifies that if the current year is a leap year, day is only counted if 29 Feb has passed
        if i % 4 != 0:
            pass
        elif i % 100 != 0:
            days += 1
        elif i % 400 != 0:
            pass
        else:
            days += 1

### Tally
days += years_ago*365

## Calculate days from months
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

### If month is same
if int(datetime.datetime.now().strftime("%m")) - int(date[1]) == 0:
    pass
### If a later month
elif int(datetime.datetime.now().strftime("%m")) - int(date[1]) > 0:
    for i in range(int(date[1]) - 1, int(datetime.datetime.now().strftime("%m")) - 1):
        days += months[i]
### If an earlier month
else:
    for i in range(int(datetime.datetime.now().strftime("%m")) - 1, int(date[1]) - 1):
        days -= months[i]

## Calulcate days from days
days += int(datetime.datetime.now().strftime("%d")) - int(date[0])

# Return results
print(f"As of {current_date}, {date[0]}/{date[1]}/{date[2]} was {days} days ago.")
