# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime
import calendar

#month, day, year
in_date = input().split()

#and it should be year,month,day
our_date = datetime.date(int(in_date[2]), int(in_date[0]), int(in_date[1]))
result = calendar.day_name[our_date.weekday()].upper()
print(result)
