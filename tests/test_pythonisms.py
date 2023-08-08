from demo.dunder import reverseString
from demo.dunder_dan import Person
  
def test_dunder_dan():
  p = Person("Anthony")
  assert p.__dan__() == "Dannthony"
  
  p = Person("Logan")
  assert p.__dan__() == "Danogan"
  
  p = Person("Sarah")
  assert p.__dan__() == "Danarah"