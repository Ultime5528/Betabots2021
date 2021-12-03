import commands2
from subsystems.troisdents import TroisDents


class Hold(commands2.CommandBase):
    def __init__(self, trois_dents: TroisDents):
        super().__init__()
        self.setName("Hold")
        self.trois_dents = trois_dents
        self.addRequirements(self.trois_dents)

    def execute(self) -> None:
        self.trois_dents.take()

    def isFinished(self) -> bool:
        return False

    def end(self, interrupted: bool) -> None:
        self.trois_dents.idle()