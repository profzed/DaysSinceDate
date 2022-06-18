# DaysSinceDate
DaysSinceDate calculates how many days has been since a specified date (0 AD onwards). It uses the dominant calendar, the Gregorian calendar.

Here is the logic:

It first takes a string input, date. This is formatted in DD/MM/YYYY. If formatted, with MM/DD/YYYY, then there may or may not be an error depending on
whether a different date following the wanted format exists. Let's say, you want to enter the 7 February 2022. You put in 02/07/2022. There will be no
error here: it will be interpreted as 2 July 2022 instead. (Note: as of writing this, it would cause an error as this day has not passed yet.) However,
if you want to enter 30 January 2022 and enter 01/30/2022, there will be an error: there is no thirtieth month.

After taking in the user input, it is converted into a list. To ensure the validity of the date, this is all encased in a while true loop with a try and
except statement. Anything that does not follow formatting/rules will cause an error and a repeat (asking for a new input, etc). Assert statements are used
to verify the validity of the date. First, it checks that the month is between one and 12 inclusive and that the year is between 0 AD and the current year
(also inclusive). It then checks days: most months have 31 or 30 days. That is simple: check the month, then check the day matches. February is a little
special though. Depending on the year, there are 29 or 28 days, as you already know (29 on leap years, 28 on common years). To make sure the day is valid,
you need to know the actual definition of a leap year.

This is the definiton for a leap in the Gregorian calendar:
  
    "The Gregorian leap year rule is: Every year that is exactly divisible by four is a leap year, except for years that are exactly
    divisible by 100, but these centurial years are leap years if they are exactly divisible by 400. For example, the years 1700, 1800,
    and 1900 are not leap years, but the year 2000 is." - United States Naval Observatory (https://aa.usno.navy.mil/faq/calendars)
    
In more simple terms:

    if (year) % 4 != 0 then
        common year
    else if (year) % 100 != 0 then
        leap year
    else if (year) % 400 != 0 then
        common year
    else
        leap year
        
After this, it verifies that it is not a future date. The loop ends with a break statement. If no errors are caused, it should reach the break statement and
exit the loop.

Now the program moves onto actually working out how many days ago that date was. First, convert the years. It works out how many years ago it was (current
year - input year). Using this, it checks every year from the input year to current year. This is almost the same as when verifying there aren't too many
days with one exception. Every time, it verifies that if 29 February has not passed this year, don't add the additional day (assuming it's the leap year).
One thing to note is: if it is 29 February, the leap day should be added. The reasion it is not added here is that this will be handled later. I'll explain
when we reach that part.

Next is the months. This is the most confusing part. I first created a list called months that stores the amount of days per month (not the actual month
name). Also, it is worthy of noting that February is stored as 28. That is because if February has passed this will have been handled by the year section.
If February has not passed, it will be handled by the day section. 

It first checks: "Is the input month the same as the current month?" If it is, this section is over. If not, it checks whether it is a later month or
earlier month. If the latter, it adds all the months (day values) that have already passed. If the former, it takes away all the months (day values) that
pass after the current month up until the current month.

Now is the days section. It simply takes away the input date from the current date. The reasion this handles the leap day when it is the 29 February is
that: 29 - 28 = 1. That simple.

The script then tallies everything up and outputs it. The intial days value from the year section would be a rough estimation: it could be higher or lower
than the actual value. The month then makes it more acurate, adding or removing extra months. That is still not accurate though so the day section does all
the fine work, adding/removing days/weeks.
