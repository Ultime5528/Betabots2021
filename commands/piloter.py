from commands2 import CommandBase

import wpilib
from wpilib._wpilib import Joystick

from constants import Proprietes
from subsystems.basepilotable import BasePilotable


class Piloter(CommandBase):
    def __init__(self, base_pilotable: BasePilotable, stick: wpilib.Joystick, xbox_controller: wpilib.Joystick):
        super().__init__()

        self.stick = stick
        self.xbox_controller = xbox_controller
        self.base_pilotable = base_pilotable
        self.addRequirements(base_pilotable)
        self.setName("Piloter")

    def execute(self):
        if Proprietes.mode_pilotage == 'joystick':
            if self.stick.getRawButton(2):
                self.base_pilotable.driveCartesian(
                    Proprietes.pilotage_max_x * self.stick.getX(),
                    Proprietes.pilotage_max_y * -self.stick.getY(),
                    Proprietes.pilotage_max_z * self.stick.getZ()
                )
            else:
                self.base_pilotable.driveCartesian(
                    Proprietes.pilotage_max_x * self.stick.getX(),
                    Proprietes.pilotage_max_y * -self.stick.getY(),
                    0.0
                )
        elif Proprietes.mode_pilotage == 'xbox gachette rotation':
            self.base_pilotable.driveCartesian(
                Proprietes.pilotage_max_x * self.xbox_controller.getX(),
                Proprietes.pilotage_max_y * -self.xbox_controller.getY(),
                Proprietes.pilotage_max_z * (self.xbox_controller.getRawAxis(3) - self.xbox_controller.getRawAxis(2))
            )
        elif Proprietes.mode_pilotage == 'xbox gachette x':
            self.base_pilotable.driveCartesian(
                Proprietes.pilotage_max_x * (self.xbox_controller.getRawAxis(3) - self.xbox_controller.getRawAxis(2)),
                Proprietes.pilotage_max_y * -self.xbox_controller.getY(),
                Proprietes.pilotage_max_z * self.xbox_controller.getX()
            )
        elif Proprietes.mode_pilotage == "xbox right stick rotation":
            self.base_pilotable.driveCartesian(
                Proprietes.pilotage_max_x * self.xbox_controller.getX(),
                Proprietes.pilotage_max_y * -self.xbox_controller.getY(),
                Proprietes.pilotage_max_z * self.xbox_controller.getRawAxis(4)
            )
        elif Proprietes.mode_pilotage == "xbox right stick x":
            self.base_pilotable.driveCartesian(
                Proprietes.pilotage_max_x * self.xbox_controller.getRawAxis(4),
                Proprietes.pilotage_max_y * -self.xbox_controller.getY(),
                Proprietes.pilotage_max_z * self.xbox_controller.getX()
            )
        else:
            self.base_pilotable.driveCartesian(0, 0, 0)

