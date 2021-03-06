from commands2 import CommandBase

import wpilib
from subsystems.basepilotable import BasePilotable
from constants import Proprietes

from networktables import NetworkTables

class AlignerPyramide(CommandBase):

    def __init__(self, base_pilotable: BasePilotable, target_x):
        super().__init__()
        self.base_pilotable = base_pilotable
        self.target_x = target_x
        self.addRequirements(base_pilotable)
        self.setName("AlignerPyramide ")
        self.max_speed = 0.15
        self.norm_x = NetworkTables.getEntry("Vision/Norm_X")

    def initialize(self):
        self.error = float("inf")

    def execute(self):
        self.error = self.norm_x.getDouble(0) - self.target_x + Proprietes.aligner_offset
        output = Proprietes.aligner_error_multiplier * self.error
        if abs(output) > Proprietes.aligner_max_speed:
            output = (self.error / abs(self.error)) * Proprietes.aligner_max_speed
        self.base_pilotable.driveCartesian(output, 0, 0)

    def end(self, interrupted: bool) -> None:
        self.base_pilotable.driveCartesian(0, 0, 0)

    def isFinished(self) -> bool:
        return abs(self.error) <= 0.05
