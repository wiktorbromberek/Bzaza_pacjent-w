from .models import Wizyta,Lekarz
from datetime import datetime
#TUTAJ TA FUNKCJA Z DATAMI

def isAvailable(lekarz, date):
    year = 2023
    month = 1
    day = 19
    hour = 18
    minutes = 00
    seconds = 00
    doctor = Lekarz.objects.get(name=lekarz)
    wizyty = Wizyta.objects.filter(lekarz=doctor,date=datetime(year,month,day,hour,minutes,seconds))
    if len(wizyty)>0:
        return False
    else:
        return True