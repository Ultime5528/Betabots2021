from commands2 import CommandBase

import wpilib

from subsystems.basepilotable import BasePilotable

class Piloter(CommandBase):
    def __init__(self, base_pilotable: BasePilotable, controller: wpilib.Joystick):
        super().__init__()

        self.controller = controller
        self.base_pilotable = base_pilotable
        self.addRequirements(base_pilotable)
        self.setName("Piloter")

    def execute(self):
        self.base_pilotable.driveCartesian(
            .5*self.controller.getX(), -0.5*self.controller.getY(), 0*self.controller.getZ()
        )