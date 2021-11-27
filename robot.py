#!/usr/bin/env python3

import commands2
import wpilib

from commands.piloter import Piloter
from commands.aller_pyramide import AllerPyramide

from subsystems.basepilotable import BasePilotable

class Robot(commands2.TimedCommandRobot):

    def robotInit(self):
        self.base_pilotable = BasePilotable()

        self.controller = wpilib.Joystick(0)

        self.base_pilotable.setDefaultCommand(Piloter(self.base_pilotable, self.controller))

        wpilib.SmartDashboard.putData("AllerPyramide", AllerPyramide(self.base_pilotable, 1))
        wpilib.SmartDashboard.putData("Commandes/Pyramide1", AllerPyramide(self.base_pilotable, 1))
        wpilib.SmartDashboard.putData("Commandes/Pyramide2", AllerPyramide(self.base_pilotable, 2))
        wpilib.SmartDashboard.putData("Commandes/Pyramide3", AllerPyramide(self.base_pilotable, 3))
        wpilib.SmartDashboard.putData("Commandes/Pyramide4", AllerPyramide(self.base_pilotable, 4))
        wpilib.SmartDashboard.putData("Commandes/Pyramide5", AllerPyramide(self.base_pilotable, 5))

        wpilib.SmartDashboard.putNumber("Proprietes/Temps Piston", 0)

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