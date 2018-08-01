"""
Made by Daniel Ginez
Main file that runs the project and integrates it in a console interface to interact with,
Temporary replaces a presentation layer
"""
from Support import functions as f

#determines the length of a plate for it to be acceptable
def mains(plateLenght, plateSeparator, dateSeparator, timeSeparator, timeLimits):
  first = True
  second = True 
  third = True
  cPlate = ""
  cDate = ""
  cTime = ""
  evaluation = "An error Ocurred"

  while True:
    if first:
      print("Please enter your plate as 'PKD"+ plateSeparator +"6692'")
      c = input()
      cPlate = f.getPlate(c, plateSeparator, plateLenght)

    if cPlate != "Plate entered incorrect" and second:
      print("Please enter your wished date as 'YYYY"+dateSeparator+"MM"+dateSeparator+"DD'")
      c = input()
      cDate = f.getDate(c,dateSeparator)
      first = False
    else:
      print(cPlate)
      print("")      
    
    if cDate != "Date entered incorrect" and third and first == False:
      print("Please enter your wished time as 'HH"+timeSeparator+"MM'")
      c = input()
      cTime = f.getTime(c,timeSeparator)
      second = False
    else:
      print(cDate)
      print("")  
    
    if cTime != "Time entered incorrect"and first == False and second == False:
      third = False
      evaluation = f.evaluate(cPlate, cDate, cTime, timeLimits, evaluation) 
      break
    else:
      print(cTime)
      print("")  
      
  print("")
  print(evaluation)

print("WELCOME TO 'WILL YOU OR HAVE YOU BEEN FINED'")
print("")

if __name__ == '__main__':
	"""The parameters sent are considered standard but can be changed to any required
  the parameters are:
  plateLenght,plateSeparator, dateSeparator, timeSeparator, timeLimits
  """
  mains(8, "-", "/", ":", [700, 930, 1600, 1930])