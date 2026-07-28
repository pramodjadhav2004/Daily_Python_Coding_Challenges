
import datetime
def count_business_days(start, end):
    weekdays=0
    startDate=datetime.datetime.strptime(start,"%Y-%m-%d")
    endDate=datetime.datetime.strptime(end,"%Y-%m-%d")
    delta=datetime.timedelta(days=1)
    while(startDate!=endDate):
        day=startDate.strftime("%A")
        if day!="Sunday" and day!="Saturday":
            weekdays+=1
        startDate=startDate+delta
    day=endDate.strftime("%A")
    day=startDate.strftime("%A")
    if day!="Sunday" and day!="Saturday":
        weekdays+=1
    return weekdays
weekdays=count_business_days("2026-02-24", "2026-02-28")
start=input("Enter start date (YYYY-MM-DD): ")
end=input("Enter end date (YYYY-MM-DD): ")
weekdays=count_business_days(start, end)
print(weekdays)