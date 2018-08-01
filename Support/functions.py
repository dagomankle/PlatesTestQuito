"""
Small file to hold individual supporting functions

"""
import arrow
from Support import plate as p
from Support import switchers as sD
import logging

def getPlate(c,plateSeparator, plateLenght):
  r = "Plate entered incorrect"

  if plateSeparator in c:
    cPlate = p.Plate(c, plateSeparator)
    if cPlate.getNumber().isdigit() and len(cPlate.getHolePlate()) == plateLenght:
      r = cPlate   
    
  return r

def getDate(c, dateSeparator):
  r = "Date entered incorrect"

  if dateSeparator in c:
    try:
      cDate= arrow.get(c)
      r = cDate
    except Exception as e :
      logging.error(e)   

  return r 

def getTime(c, timeSeparator):
  r = "Time entered incorrect"

  if timeSeparator in c and " " not in c:
    try:
      c = int(c.replace(timeSeparator, ""))
      r = c 
    except Exception as e:
      logging.error(e)    

  return r  

def evaluate(plate, date, time, timeLimits, evaluation):
  switch = sD.SwitcherDay()
  weekDay = date.weekday()

  if weekDay == 5 or weekDay == 6 or int(weekDay) != int(switch.plate_to_days(plate.getSignificantNumber())) :
    evaluation = "You can drive that hole day without a worry"
  elif (time >= timeLimits[0] and time < timeLimits[1]) or (time >= timeLimits[2] and time < timeLimits[3]):
    evaluation = "You can't drive at that time" 
  else:   
    evaluation = "You can drive that day but be carefull you have restrictions today"

  return evaluation