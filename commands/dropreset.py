from subsystems.troisdents import TroisDents
import commands2
from commands.reset import Reset
from commands.drop import Drop


class DropReset(commands2.SequentialCommandGroup):
    def __init__(self, trois_dents: TroisDents):
        super().__init__([
            Drop(trois_dents),
            Reset(trois_dents)
        ])
        self.setName("DropReset")
