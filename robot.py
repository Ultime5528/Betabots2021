#!/usr/bin/env python3

import commands2
import wpilib
from commands2.button import JoystickButton

from commands.drop import Drop
from commands.dropreset import DropReset
from commands.hold import Hold
from commands.piloter import Piloter
from commands.aller_pyramide import AllerPyramide
from commands.reset import Reset
from commands.troisdents_idle import TroisDentsIdle

from subsystems.basepilotable import BasePilotable
from subsystems.troisdents import TroisDents

from commands2.button import JoystickButton


class Robot(commands2.TimedCommandRobot):

    def robotInit(self):
        wpilib.CameraServer.launch('vision.py:main')
        self.base_pilotable = BasePilotable()
        self.troisdents = TroisDents()

        self.controller = wpilib.Joystick(0)
        JoystickButton(self.controller, 1).whenPressed(Drop(self.troisdents))
        JoystickButton(self.controller, 2).whenPressed(Hold(self.troisdents))
        JoystickButton(self.controller, 3).whenPressed(Reset(self.troisdents))
        JoystickButton(self.controller, 4).whenPressed(TroisDentsIdle(self.troisdents))
        JoystickButton(self.controller, 5).whenPressed(DropReset(self.troisdents))

        self.base_pilotable.setDefaultCommand(Piloter(self.base_pilotable, self.controller))
        JoystickButton(self.controller, 3).whenPressed(AllerPyramide(self.base_pilotable, 0.0))



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