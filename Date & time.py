# Date & times

import datetime

date = datetime.date(2026, 3, 24)
today = datetime.date.today()

time = datetime.time(12, 45, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %d-%m-%Y")


target_datetime = datetime.datetime(2017, 3, 8, 12, 15, 35)
current_datetime = datetime.datetime.now()

if current_datetime > target_datetime:
    print("Taget date has passed")
else:
    print("Target date has NOT passed")