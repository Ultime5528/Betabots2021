from commands2 import CommandBase

import wpilib

from subsystems.basepilotable import BasePilotable

class AllerPyramide(CommandBase):
    def __init__(self, base_pilotable: BasePilotable, colonne: int):
        super().__init__()

        self.base_pilotable = base_pilotable
        self.colonne = colonne
        self.addRequirements(base_pilotable)
        self.timer = wpilib.Timer()
        self.setName("AllerPyramide " + str(self.colonne))

    def initialize(self):
        self.timer.reset()
        self.timer.start()

    def execute(self):
        print(self.colonne)

    def isFinished(self):
        return self.timer.get() > 10
