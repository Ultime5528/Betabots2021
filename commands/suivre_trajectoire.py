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
        transform = self.end_position - self.drive.odometry.getPose()
        x_speed = self.speed
        y_speed = self.speed
        turn_speed = 0.1
        dx = transform.X()
        dy = transform.Y()
        dtheta_degrees = transform.rotation().degrees()
        if abs(dx) <= 0.1:
            x_speed = 0.0
        if abs(dy) <= 0.1:
            y_speed = 0.0
        if abs(dtheta_degrees) <= 3:
            turn_speed = 0.0
        self.drive.driveCartesian(math.copysign(y_speed, -dy), math.copysign(x_speed, dx), math.copysign(turn_speed, -dtheta_degrees))

    def isFinished(self) -> bool:
        distance = self.drive.odometry.getPose().translation().distance(self.end_position.translation())
        return distance <= 0.15 and abs(self.drive.odometry.getPose().rotation().degrees() - self.end_position.rotation().degrees()) < 2

    def end(self, interrupted: bool) -> None:
        self.drive.driveCartesian(0, 0, 0)
