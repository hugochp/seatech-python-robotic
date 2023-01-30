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

    def go_front(self, coef):

        self.__left_wheel.activeMotorForward(coef)
        self.__right_wheel.activeMotorForward(coef)

    def go_back(self, coef):

        self.__left_wheel.activeMotorBackward(coef)
        self.__right_wheel.activeMotorBackward(coef)

robot = Robot()

timestep = int(robot.getBasicTimeStep())

robot_Control = RobotControl()

while robot.step(timestep) != -1:

    robot_Control.go_front(0.5)  # to move forward
    robot.step(timestep)

