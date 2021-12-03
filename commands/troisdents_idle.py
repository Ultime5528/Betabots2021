import commands2
from subsystems.troisdents import TroisDents


class TroisDentsIdle(commands2.CommandBase):
    def __init__(self, trois_dents: TroisDents):
        super().__init__()
        self.setName("TroisDentsIdle")
        self.trois_dents = trois_dents
        self.addRequirements(self.trois_dents)

    def isFinished(self) -> bool:
        return True

    def end(self, interrupted: bool) -> None:
        self.trois_dents.idle()