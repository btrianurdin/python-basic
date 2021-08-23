# define class in python
class Vehicle:

  # define constructor (__init__)
  # always executed when the class is being initiated
  def __init__(self, type, plates, year):
    # create public property
    self.type = type
    self.year = year
    # create private property 
    # (added a double underscore at the beginning of the method name)
    self.__plates = plates

  def info(self):
    # call and print property
    print("Vehicle Type: " + self.type)
    print("Vehicle Year: " + self.year)
    print("Vehicle Plates: " + self.__plates)

  def start(self):
    print("vehicle is start")

  # define method with return statement
  def stop(self):
    print("vehicle is stop")


# define object
car = Vehicle("Honda Jazz", "AB 2766 UI", "2019")
car.info()

# change property value
car.type = "Avanza"
car.year = "2020"
car.__plates = "E 7736 HH" # not change because this property is private
car.info()

car.start()
car.stop()
