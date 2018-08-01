import unittest
import arrow
from Support import plate as p
from Support import functions as f

class TestSupportMethods(unittest.TestCase):

  def testEvaluate(self):
    plate = p.Plate("asd-1546")
    date = arrow.get("2018/08/01")
    self.assertEqual(f.evaluate(plate, date, 730, [700, 930, 1600, 1930], "" ), "You can't drive at that time")

  def testPlate(self):
    plate = p.Plate("asd-1546")

    self.assertEqual(plate.getNumber(), "1546")
    self.assertEqual(plate.getData(), "asd")
    self.assertEqual(plate.getHolePlate(), "asd-1546")
    self.assertEqual(str(plate), "asd-1546")

  def testGetPlate(self):
    plate = p.Plate("asd-1546")
    self.assertEqual(f.getPlate("asd-1546", "-"), plate)

  def testGetDate(self):
    date = arrow.get("2018/08/01")
    self.assertEqual(f.getDate("2018/08/01", "/"), date)

  def testGetTime(self):
    self.assertEqual(f.getTime("07:30", ":"), 730)

if __name__ == '__main__':
  unittest.main()