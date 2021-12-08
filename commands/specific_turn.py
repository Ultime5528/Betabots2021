import commands2
from subsystems.basepilotable import BasePilotable

class SpecificTurn(commands2.CommandBase):
    def __init__(self, angle: float, drive: BasePilotable, turn_speed: float):
        super().__init__()
        self.angle = angle
        self.drive = drive
        self.turn_speed = turn_speed
        self.addRequirements(self.drive)

    def initialize(self):
        self.drive.resetOdometry()

    def execute(self):
        self.drive.driveCartesian(0, 0, self.turn_speed)

    def end(self, interrupted: bool):
        self.drive.driveCartesian(0, 0, 0)

    def isFinished(self) -> bool:
        return abs(self.drive.getAngle() - self.angle) <= 2