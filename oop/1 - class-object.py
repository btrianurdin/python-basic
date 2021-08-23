# define class in python
class Vehicle:
  
  # define method in class
  # @params self is a required parameter every define method in a class
  def start(self):
    print("vehicle is start")

  # define method with spee d parameter
  def run(self, speed):
    # casting parameter to string
    speed_str = str(speed)

    # call and print speed parameter 
    print("vehicle is run with speed " + speed_str + "km/h")

  # define method with return statement
  def stop(self):
    return "vehicle is stop"


# define object 
car = Vehicle()

car.start()
car.run(30)
car.stop()
# call stop method and print 
print(car.stop())
