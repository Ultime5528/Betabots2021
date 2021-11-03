#!/usr/bin/env python3

import commands2
import wpilib
from commands2 import CommandScheduler

from commands.piloter import Piloter

from subsystems.basepilotable import BasePilotable

class Robot(commands2.TimedCommandRobot):

    def robotInit(self):
        self.base_pilotable = BasePilotable()

        self.controller = wpilib.Joystick(0)

        self.base_pilotable.setDefaultCommand(Piloter(self.base_pilotable, self.controller))

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        pass


if __name__ == "__main__":
    wpilib.run(Robot)