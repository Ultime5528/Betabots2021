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
        self.max_speed = 0.1
        self.norm_x = NetworkTables.getEntry("Vision/Norm_X")


    def execute(self):
        self.error = self.norm_x.getDouble(0) - self.target_x
        ouput = 2 * self.error
        if abs(ouput) > self.max_speed:
            output = (self.error / abs(self.error)) * self.max_speed

        self.base_pilotable.driveCartesian(output, 0, 0)

    def end(self, interrupted: bool) -> None:
        self.base_pilotable.driveCartesian(0, 0, 0)

    def isFinished(self) -> bool:
        return abs(self.error) <= 0.05

    

