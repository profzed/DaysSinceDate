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

        # Enforces that days be between 1 and 31 inclusive, months be between 1 and 12 inclusive and years be from 0 AD up until the current year
        assert int(date[0]) <= 31 and int(date[0]) > 00 and int(date[1]) <= 12 and int(date[1]) > 00 and int(date[2]) <= int(datetime.datetime.now().strftime("%Y")) and int(date[2]) >= 0000

        break
    except:
        print("Invalid input: dates should be formatted DD/MM/YYYY")

# Calculate how long ago that was

## Calculate days from years
years_ago = int(datetime.datetime.now().strftime("%Y")) - int(date[2])

### Calculate leap days
leap_days = 0
for i in range(int(date[2]), int(datetime.datetime.now().strftime("%Y")) + 1):
    if int(datetime.datetime.now().strftime("%m")) > 2: # verifies that if the current year is a leap year, day is only counted if 29 Feb has passed
        if i % 4 != 0:
            pass
        elif i % 100 != 0:
            leap_days += 1
        elif i % 400 != 0:
            pass
        else:
            leap_days += 1

### Tally
days_years = years_ago*365 + leap_days

## Calculate days from months
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_months = 0

### If month is same
if int(datetime.datetime.now().strftime("%m")) - int(date[1]) == 0:
    pass
### If a later month
elif int(datetime.datetime.now().strftime("%m")) - int(date[1]) > 0:
    for i in range(int(date[1]) - 1, int(datetime.datetime.now().strftime("%m")) - 1):
        days_months += months[i]
### If an earlier month
else:
    for i in range(int(datetime.datetime.now().strftime("%m")) - 1, int(date[1]) - 1):
        days_months -= months[i]

## Calulcate days from days
days_days = int(datetime.datetime.now().strftime("%d")) - int(date[0])

## Tally up total days
days = days_years + days_months + days_days

# Return results
print(f"As of {current_date}, {date[0]}/{date[1]}/{date[2]} was {days} days ago.")
