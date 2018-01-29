from datetime import datetime

import pytz

utc = pytz.utc
#utc is the Coordinated Universal TIme

ist = pytz.timezone('Asia/Kolkata')
#ist is the Indain Standard Time

now = datetime.now(tz=utc)
#this is the current time in utc

ist_now = now.astimezone(ist)
#this is the current timezone in ist
