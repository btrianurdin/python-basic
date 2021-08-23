# define class in python
class Vehicle:
  
  def __init__(self, type, plates, year):
    # public property
    self.type = type
    # private property
    self.__year = year
    self.__plates = plates

  # define getter for year property
  @property
  def year(self):
    return self.__year
  
  # define setter for type property
  @year.setter
  def year(self, new_year):
    # do validation before assign value to year property
    # year must be int not string
    if isinstance(new_year, int):
      self.__year = new_year
    else:
      print("Year not valid!")

  # define getter for plates property
  @property
  def plates(self):
    return self.__plates

  # define setter for plates property
  @plates.setter
  def plates(self, new_plates):
    self.__plates = new_plates
  
  def info(self):
    # call and print property
    print("Vehicle Type: " + self.type)
    print("Vehicle Year: " + self.year)
    print("Vehicle Plates: " + self.__plates)


# define object and run class
car = Vehicle("Tesla S3", "B 88 EE", "2020")

car.info()

# change property value
car.year = "baah" # will be catch message "Year not valid!"
car.year = 2021
car.plates = "B 00 TT"

# print with getter
print("Type: " + car.type)
print("New year after change: " + str(car.year))
print("New plates after change: " + car.plates)