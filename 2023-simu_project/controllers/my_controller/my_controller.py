from controller import Robot, Motor

# Create a new robot
robot = Robot()

# Get the time step of the simulation
timestep = int(robot.getBasicTimeStep())

# Get the left and right wheel motors
leftMotor = robot.getDevice("LLegKny")
rightMotor = robot.getDevice("RLegKny")

# Set the target position of the motors
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
x = 0
# Main loop
while robot.step(timestep) != -1:
    # Set the velocity of the motors
    x += 0.1
    leftMotor.setVelocity(cos(x))
    rightMotor.setVelocity(-cos(x))