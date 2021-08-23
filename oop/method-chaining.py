class Calculator:

  def __init__(self, value):
    self.__value = value
  
  def add(self, value):
    self.__value += value

    return self

  def subtract(self, value):
    self.__value -= value

    return self

  def multiply(self, value):
    self.__value *= value

    return self
  
  def result(self):
    print(self.__value)

# mendefinisikan object kalkuator
calc = Calculator(20)

calc.multiply(20).subtract(5).result()