import math

import commands2
from subsystems.basepilotable import BasePilotable
from wpimath.geometry import Pose2d
from termcolor import colored
import math


class SuivreTrajectoire(commands2.CommandBase):
    def __init__(self, drive: BasePilotable, end_position: Pose2d) -> None:
        super().__init__()
        self.drive = drive
        self.addRequirements(self.drive)
        self.end_position = end_position

    def initialize(self) -> None:
        self.drive.resetOdometry()

    def execute(self) -> None:
        twist = self.drive.odometry.getPose().log(self.end_position)
        hypotenuse = math.hypot(twist.dx, twist.dy)
        print(colored(twist.dx/hypotenuse, "green"))
        speed = 0.4
        turn_speed = 0.05
        self.drive.driveCartesian(-speed * twist.dy / hypotenuse, speed * twist.dx / hypotenuse, math.copysign(turn_speed, -twist.dtheta_degrees))

    def isFinished(self) -> bool:
        print(colored(self.drive.odometry.getPose().translation().distance(self.end_position.translation()), "yellow"))
        distance = self.drive.odometry.getPose().translation().distance(self.end_position.translation())
        return distance <= 0.25

    def end(self, interrupted: bool) -> None:
        print(colored("Finish", "red"))
        self.drive.driveCartesian(0, 0, 0)
