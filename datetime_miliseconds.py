import pytz
from datetime import datetime

# Author: Adrian Ojeda
# Convert from a given miliseconds datetime to datetime object
# and convert it in a specific timezone

est_tmz = pytz.timezone('America/New_York')
fmt = "%Y-%m-%d %H:%M:%S %Z%z"

# e.x date in miliseconds.
# Value in UTC: Wednesday, January 31, 2018 6:00:00 AM UTC
# Checkout value here: https://www.fileformat.info/tip/java/date2millis.htm
ms = 1517378400000
#convert ms in datetime object in UTC timezone
ms_datetime = datetime.utcfromtimestamp(ms//1000).replace(tzinfo=pytz.utc, microsecond=ms%1000*1000)

#convert in EST timezone
ms_datetime_tmz = est_tmz.normalize(ms_datetime.astimezone(est_tmz))
ms_datetime_tmz.strftime(fmt)

#converted datetime
print("-----------------------------")
print(ms_datetime_tmz.strftime(fmt))
print("-----------------------------")

print("")
#########################################################################

# Convert the current server datetime in a given timezone

# Get current server datetime in UTC
now_utc = datetime.now(pytz.timezone('UTC'))
# convert now datetime in EST timezone
now_est = now_utc.astimezone(est_tmz)

print("-----------------------------")
print(now_utc.strftime(fmt))
print("-----------------------------")
print(now_est.strftime(fmt))
print("-----------------------------")


