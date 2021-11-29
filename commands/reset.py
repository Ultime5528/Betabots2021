import wpilib
import commands2
from subsystems.troisdents import TroisDents


class Reset(commands2.CommandBase):
    def __init__(self, trois_dents: TroisDents):
        super().__init__()
        self.setName("Reset")
        self.trois_dents = trois_dents
        self.timer = wpilib.Timer()
        self.addRequirements(self.trois_dents)
        self.timer = wpilib.Timer()

    def initialize(self) -> None:
        self.timer.reset()
        self.timer.start()

    def execute(self) -> None:
        self.trois_dents.take()

    def isFinished(self) -> bool:
        return self.timer.get() >= 1

    def end(self, interrupted: bool) -> None:
        self.trois_dents.idle()
