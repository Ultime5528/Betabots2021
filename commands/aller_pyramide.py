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
        self.max_speed = 0.15
        self.norm_x = NetworkTables.getEntry("Vision/Norm_X")

    def initialize(self):
        self.error = float("inf")

    def execute(self):
        wpilib.SmartDashboard.putNumber("accelX", self.base_pilotable.getAccelX())
        wpilib.SmartDashboard.putNumber("accelY", self.base_pilotable.getAccelY())
        wpilib.SmartDashboard.putNumber("accelZ", self.base_pilotable.getAccelZ())
        wpilib.SmartDashboard.putBoolean("isMoving", self.base_pilotable.isMoving())
        self.error = self.norm_x.getDouble(0) - self.target_x
        output = 1.5 * self.error
        if abs(output) > self.max_speed:
            output = (self.error / abs(self.error)) * self.max_speed
        self.base_pilotable.driveCartesian(output, 0, 0)

    def end(self, interrupted: bool) -> None:
        self.base_pilotable.driveCartesian(0, 0, 0)

    def isFinished(self) -> bool:
        return abs(self.error) <= 0.05
