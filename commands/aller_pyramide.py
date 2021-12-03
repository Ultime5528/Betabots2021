from commands2 import CommandBase

import wpilib

from subsystems.basepilotable import BasePilotable

from networktables import NetworkTables

class AllerPyramide(CommandBase):
    def __init__(self, base_pilotable: BasePilotable, target_x):
        super().__init__()

        self.base_pilotable = base_pilotable
        self.target_x = target_x
        self.addRequirements(base_pilotable)
        self.setName("AllerPyramide ")
        self.norm_x = NetworkTables.getEntry("Vision/Norm_X")

    def initialize(self):
        self.drive.resetEncoders()

    def execute(self):
        self.error = self.norm_x.getDouble() - target_x
        self.base_pilotable.driveCartesian(self.error, 0, 0) 

    def end(self, interrupted: bool) -> None:
        self.drive.driveCartesian(0, 0, 0)

    def isFinished(self) -> bool:
        return abs(self.error) <= 0.05

    

