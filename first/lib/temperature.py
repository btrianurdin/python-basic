from typing import Union

class Temperature:
  __temp_convert = {
    "celsius": False,
    "fahrenheit": False,
    "kelvin": False
  }

  def __init__(self, celcius = 0, fahrenheit = 0, kelvin = 0):
      self.__celcius = celcius
      self.__fahrenheit = fahrenheit
      self.__kelvin = kelvin

  def celcius(self, value:int = None):
    if value is not None:
      self.__celcius = value
    
    self.__temp_convert['celcius'] = True
    return self
  
  def fahrenheit(self, value: int = None):
    if value is not None:
      self.__fahrenheit = value

    self.__temp_convert['fahrenheit'] = True
    return self

  def kelvin(self, value: int = None):
    if value is not None:
      self.__kelvin = value

    self.__temp_convert['kelvin'] = True
    return self

  def __check_temp_active(self) -> str:
    for x in self.__temp_convert:
      if self.__temp_convert[x] is True:
        return x
      
  def __clear_tmp_active(self):
    for x in self.__temp_convert:
      self.__temp_convert[x] = False

  def toFahrenheit(self, with_symbol=False) -> str:
    check: str = self.__check_temp_active()
    count = {
      "celcius": (9/5)*self.__celcius+32,
      "kelvin": (9/5)*(self.__kelvin-273)+32
    }
    self.__clear_tmp_active()

    return str(count.get(check, self.__fahrenheit)) + ('\N{DEGREE SIGN}F' if with_symbol else '')

  def toCelcius(self, with_symbol=False) -> str:
    check: str = self.__check_temp_active()
    count = {
      "fahrenheit": (5/9)*(self.__fahrenheit-32),
      "kelvin": self.__kelvin-273
    }
    self.__clear_tmp_active()

    return str(count.get(check, self.__celcius)) + ('\N{DEGREE SIGN}C' if with_symbol else '')

  def toKelvin(self, with_symbol=False) -> str:
    check: str = self.__check_temp_active()
    count = {
        "celcius": self.__celcius+273,
        "fahrenheit": (5/9)*(self.__fahrenheit-32)+273
    }
    self.__clear_tmp_active()

    return str(count.get(check, self.__kelvin)) + ('\N{DEGREE SIGN}K' if with_symbol else '')

  @staticmethod
  def symbol(text: str) -> str:
    return '\N{DEGREE SIGN}' + text
