def hours2days(hours):
     
     days = int(hours//24)
     hour = hours%24
     
     return days,hour
     
print(hours2days(5002))
     
