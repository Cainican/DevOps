##########################
#   datetime-sample.py   #
#        P. 163          #
##########################

# Importere datetime
import datetime

# Print current date
#print(datetime.date.today())

# Print current date and time (year, month, date, hour, minute, second, microsecond)
#print(datetime.datetime.now())

d = datetime.datetime.today()
print(d.strftime("%Y年%m月%d日%A"))