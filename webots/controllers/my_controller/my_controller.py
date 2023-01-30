import math
from controller import Robot, Motor

class WholeRobotMotor(Motor) :

    def __init__(self, name = None):

        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)

    def activeMotorForward(self, coef):

        self.setVelocity(coef * 9.53)

    def activeMotorBackward(self, coef):

        self.setVelocity(coef * (-9.53))


class RobotControl():

    def __init__(self):

        self.__left_wheel = WholeRobotMotor('motor.left')
        self.__right_wheel = WholeRobotMotor('motor.right')
        self.__time = 0

    def go_front(self, coef):

        self.__left_wheel.activeMotorForward(coef)
        self.__right_wheel.activeMotorForward(coef)

    def go_back(self, coef):

        self.__left_wheel.activeMotorBackward(coef)
        self.__right_wheel.activeMotorBackward(coef)

    def go_left(self, coef):

        self.__left_wheel.activeMotorForward(coef)

    def go_right(self, coef):

        self.__right_wheel.activeMotorBackward(coef)

    def move_in_eight(self, A, B, coef):
        
        x = A * math.cos(B * self.__time)/2
        y = A * math.sin(B * self.__time)

        # Left wheel moves forward or backward depending on x
        if x > 0:
            self.__left_wheel.activeMotorForward(x * coef)
        else:
            self.__left_wheel.activeMotorBackward(-x * coef)

        # Right wheel moves forward or backward depending on y
        if y > 0:
            self.__right_wheel.activeMotorForward(y * coef)
        else:
            self.__right_wheel.activeMotorBackward(-y * coef)

        self.__time += 0.01

robot = Robot()
timestep = int(robot.getBasicTimeStep())
robot_Control = RobotControl()

while robot.step(timestep) != -1:
    robot_Control.move_in_eight(1, 2, 1) # move in eight shape
    robot.step(timestep)