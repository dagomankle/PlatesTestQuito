"""
Class to facilitate plates management
Data obtained from : https://es.wikipedia.org/wiki/Matr%C3%ADculas_automovil%C3%ADsticas_de_Ecuador
Has to have the type XXX%0000 where x is a letter and 0 a positive digit and % is a separator 
between the metadata and the plate number
"""
class Plate:

  def __init__(self, incoming, plateSeparator):
    #Double underscore is used to keep the Encapsulation
    self.__holePlate = incoming
    h = incoming.split(plateSeparator)
    self.__data = h[0]
    self.__number = h[1]

  def getNumber(self ):
    return self.__number

  def getData(self ):
    return self.__data

  def getHolePlate(self ):
    return self.__holePlate

  def getSignificantNumber(self):
    return self.__holePlate[-1]

  def __str__(self):
    return self.__holePlate