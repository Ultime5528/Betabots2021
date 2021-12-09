import math

import commands2
from subsystems.basepilotable import BasePilotable
from wpimath.geometry import Pose2d


class SuivreTrajectoire(commands2.CommandBase):
    def __init__(self, drive: BasePilotable, end_position: Pose2d, speed: float) -> None:
        super().__init__()
        self.drive = drive
        self.addRequirements(self.drive)
        self.end_position = end_position
        self.speed = speed

    def initialize(self) -> None:
        self.drive.resetOdometry()

    def execute(self) -> None:
        twist = self.drive.odometry.getPose().log(self.end_position)
        hypotenuse = math.hypot(twist.dx, twist.dy)
        turn_speed = 0.1
        if abs(twist.dtheta_degrees) <= 3:
            turn_speed = 0.0
        self.drive.driveCartesian(-self.speed * twist.dy / hypotenuse, self.speed * twist.dx / hypotenuse, math.copysign(turn_speed, -twist.dtheta_degrees))

    def isFinished(self) -> bool:
        distance = self.drive.odometry.getPose().translation().distance(self.end_position.translation())
        return distance <= 0.1 and abs(self.drive.odometry.getPose().rotation().degrees() - self.end_position.rotation().degrees()) < 2

    def end(self, interrupted: bool) -> None:
        self.drive.driveCartesian(0, 0, 0)
