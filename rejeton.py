import wpilib
from wpilib._wpilib import CAN
import wpilib.drive
import rev

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        
        self.left_motor = rev.CANSparkMax(1, rev.MotorType.kBrushless)
        self.left2_motor = rev.CANSparkMax(2, rev.MotorType.kBrushless)
        self.left = wpilib.SpeedControllerGroup(self.left_motor, self.left2_motor)

        self.right_motor = rev.CANSparkMax(3, rev.MotorType.kBrushless)
        self.right2_motor = rev.CANSparkMax(4, rev.MotorType.kBrushless)
        self.right = wpilib.SpeedControllerGroup(self.right_motor, self.right2_motor)
        self.vis = wpilib.VictorSP(0)

        self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)

        self.stick = wpilib.Joystick(0)

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.drive.arcadeDrive(-self.stick.getY(), self.stick.getX())

        if self.stick.getRawButton(1):
            self.vis.set (1.0)
        elif self.stick.getRawButton(2):
            self.vis.set (-1.0)
        else: self.vis.set (0.0)
            


if __name__ == "__main__":
    wpilib.run(MyRobot)
