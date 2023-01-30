from controller import Robot, Motor

class WholeRobotMotor(Motor) :

    def __init__(self, name = None):

        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)

    def activeMotorForward(self):

        self.setVelocity(9.53)

    def activeMotorBackward(self):

        self.setVelocity(-9.53)


class RobotControl():

    def __init__(self):

        self.__left_wheel = WholeRobotMotor('motor.left')
        self.__right_wheel = WholeRobotMotor('motor.right')

    def go_front(self):

        self.__left_wheel.activeMotorForward()
        self.__right_wheel.activeMotorForward()

    def go_back(self):

        self.__left_wheel.activeMotorBackward()
        self.__right_wheel.activeMotorBackward()

robot = Robot()

timestep = int(robot.getBasicTimeStep())

robot_Control = RobotControl()

while robot.step(timestep) != -1:

    robot_Control.go_front()  # to move forward
    robot.step(timestep)

