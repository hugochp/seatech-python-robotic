from time import sleep

class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutdown', 'running']
    __charging_state = False
        
    def __init__(self, name = "<unnamed>"):

      self.__name = name

    def setName(self, name):

      self.__name = name

    def getName(self):

      return self.__name

    def setPower(self, power):

      self.__power = power

    def getPower(self):

      return self.__power

    def setChargingState(self, state):

      self.__charging_state = state

    def setBatteryLevel(self, batteryLevel):

      if batteryLevel <= 100 and batteryLevel >= 0:
        self.__battery_level = batteryLevel

    def getBatteryLevel(self):

      return self.__battery_level

    def setCurrentSpeed(self, currentSpeed):

      if currentSpeed <= 10:
        self.__current_speed = currentSpeed

    def getCurrentSpeed(self):

      return self.__current_speed

    def getState(self):

      if self.getPower() == True:
        return self.__states[1]

      elif self.getPower() == False:
        return self.__states[0]

      else :
        return None

    def boot(self):

      if self.__power == False:
        self.__power = True

      elif self.__power == True:
        print("Already Booted")

      else:
        print("Power undefined")

    def shutdown(self):

      if self.__power == True:
        self.__power = False

      elif self.__power == False:
        print("Already Shutdowned")

      else:
        print("Power undefined")

    def displayBatteryLevel(self):

      print("Battery Level : " + str(self.__battery_level) + " %")

    def increaseBatteryLevel(self):

      if self.__battery_level <= 100 and self.__battery_level >= 0 :
        self.__battery_level += 10

    def displayMovingSpeed(self):

      print("Moving Speed : " + str(self.__current_speed) + " km/h")

    def stopMoving(self):

      self.setCurrentSpeed(0)

    def update(self):

      print("///")
      self.displayBatteryLevel()
      self.displayMovingSpeed()
      print("///")
      sleep(1)
      if self.__charging_state == True:
        self.increaseBatteryLevel()
      else:
        self.__battery_level -= 1

if __name__ == "__main__" :

  r = Robot("Roberto")
  r.boot()
  r.setChargingState(True)

  for i in range(10):
    r.update()

  r.setChargingState(False)
  r.setCurrentSpeed(5)

  for i in range(5):
    r.update()

  r.shutdown()