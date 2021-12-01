from commands2 import CommandBase

import wpilib
from wpilib._wpilib import Joystick

from subsystems.basepilotable import BasePilotable

a = ''

class Piloter(CommandBase):
    def __init__(self, base_pilotable: BasePilotable, controller: wpilib.Joystick):
        super().__init__()
        
        self.controller = controller
        self.base_pilotable = base_pilotable
        self.addRequirements(base_pilotable)
        self.setName("Piloter")

    def execute(self):
        if a=='':
            if self.controller.getRawButton(2):
                self.base_pilotable.driveCartesian(
                    self.controller.getX(), self.controller.getY(), self.controller.getZ()
                )
            else:
                self.base_pilotable.driveCartesian(
                    self.controller.getX(), self.controller.getY(), 0.0
                )
        elif a=='':
            if self.controller.getRawButton(2):
                self.base_pilotable.driveCartesian(
                    self.controller.getX(), self.controller.getY(), 0.0
                )
            else:
                self.base_pilotable.driveCartesian(
                    self.controller.getX(), self.controller.getY(), self.controller.getZ()
                )
        elif a=='':
            
            if self.controller.getRawButton(1):
                self.base_pilotable.driveCartesian(
                self.controller.getX(), self.controller.getY(), 1.0
                )
            elif self.controller.getRawButton(2):
                self.base_pilotable.driveCartesian(
                    self.controller.getX(), self.controller.getY(), -1.0
                )
        elif a=='':
            self.base_pilotable.driveCartesian(
                self.controller.getY(), self.controller.getZ(), 0.0
            )
            if self.controller.getRawButton(1):
                self.controller.getY(), self.controller.getZ(), 1.0

            elif self.controller.getRawButton(2):
                self.controller.getY(), self.controller.getZ(), -1.0
