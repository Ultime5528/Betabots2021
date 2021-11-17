import wpilib
import commands2
from subsystems.basepilotable import BasePilotable

class DriveDistance(commands2.CommandBase):
    def __init__(self, drive: BasePilotable, centimeters: float, speed: float) -> None:
        super().__init__()
        self.drive = drive
        self.distance = centimeters
        self.speed = speed
        self.drive = drive
        self.addRequirements([drive])

    def initialize(self) -> None:
        self.drive.resetEncoders()

    def execute(self) -> None:
        self.drive.driveCartesian(0, self.speed, 0)

    def end(self, interrupted: bool) -> None:
        self.drive.driveCartesian(0, 0, 0)

    def isFinished(self) -> bool:
        return self.drive.getAverageEncoderDistance() >= self.distance
