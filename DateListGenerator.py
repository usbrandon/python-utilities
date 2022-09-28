import time
import math
from datetime import date, timedelta
import datetime

StartDate = datetime.datetime(2022, 1, 1)
EndDate = datetime.datetime(2022, 12, )
DaysBetween = 7
print(f"Start Date is {StartDate}.")
print(f"End Date is {EndDate}.")

# Units in days and performed all days inclusively
# i.e. later date minus earlier date; add back a day for the earlier date
TimeSpan = (EndDate - StartDate).days + 1
print(TimeSpan)

# This is how many times we will need to loop through the math to create date
# parameter pairs
TimeSegments = math.ceil(TimeSpan / DaysBetween)
print(TimeSegments)

frac = TimeSpan % DaysBetween * DaysBetween
print(frac)

# Our list will begin with the StartDate
dateList = [StartDate]

# Prepare the next End Date in the sequence
nextDate = StartDate + timedelta(days=DaysBetween - 1)
for loopPassNum in range(TimeSegments):
    print(loopPassNum)
    # We started with the first element in the list added, the next prepped, we add it here.
    if (dateList[-1] != EndDate):
        dateList.append(nextDate)
    # Now we prepare the next start date, one more than the End Date we added to the prior pair.
    nextDate = nextDate + timedelta(days=1)
    if dateList[-1] != EndDate:
        if len(dateList) % 2 != 0 or dateList[-1] != EndDate:
            dateList.append(nextDate)

    if dateList[-1] < EndDate:
        if nextDate + timedelta(days=DaysBetween - 1) >= EndDate:
            nextDate = EndDate
        else:
            nextDate = nextDate + timedelta(days=DaysBetween - 1)


# This is a special case. Our list consists of pairs of start and end dates for a report parameter
# If the date list has an odd number of elements, it means we are missing an ending date.
if len(dateList) % 2 == 0:
    print("even: do nothing")
else:
    print("Topping off our date list with an end date (last date appended.")
    nextDate = dateList[-1]
    dateList.append(nextDate)


print(dateList)

print("Running through the dates\n")
print("Length of dateList is ", len(dateList))
for eachDate in dateList:
    print(eachDate.strftime("%Y-%m-%d"))
