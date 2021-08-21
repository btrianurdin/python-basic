def convert(menu, temp):
  switcher = {
      1: from_celcius,
      2: from_fahrenheit,
      3: from_kelvin
  }

  return switcher[menu](temp)

def from_celcius(C):
  print(C, "\N{DEGREE SIGN}C = ", (9/5)*C+32, "\N{DEGREE SIGN}F")
  print(C, "\N{DEGREE SIGN}C = ", C+273, "\N{DEGREE SIGN}K")

def from_fahrenheit(F):
  print(F, "\N{DEGREE SIGN}F = ", (5/9)*(F-32), "\N{DEGREE SIGN}C")
  print(F, "\N{DEGREE SIGN}F = ", (5/9)*(F-32)+273, "\N{DEGREE SIGN}K")

def from_kelvin(K):
  print(K, "\N{DEGREE SIGN}K = ", K-273, "\N{DEGREE SIGN}C")
  print(K, "\N{DEGREE SIGN}K = ", (9/5)*(K-273)+32, "\N{DEGREE SIGN}F")
