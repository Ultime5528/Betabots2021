import commands2
from wpimath.geometry import Pose2d, Rotation2d

from commands.aligner_pyramide import AlignerPyramide
from commands.hold import Hold
from commands.dropreset import DropReset
from commands.suivre_trajectoire import SuivreTrajectoire
from commands.aller_pyramide import AllerPyramide
from commands.specific_turn import SpecificTurn

from subsystems.troisdents import TroisDents
from subsystems.basepilotable import BasePilotable


class AutoJaune(commands2.SequentialCommandGroup):
    def __init__(self, troisdent: TroisDents, base_pilotable: BasePilotable):
        super().__init__(
            commands2.ParallelDeadlineGroup(
                commands2.SequentialCommandGroup(
                    commands2.WaitCommand(0.5),
                    SpecificTurn(90, base_pilotable, -0.15),
                    SuivreTrajectoire(base_pilotable, Pose2d(4, 0.75, Rotation2d.fromDegrees(0)), 0.19),
                    SpecificTurn(-45, base_pilotable, 0.15),
                    AllerPyramide(base_pilotable, 0.0, 10),
                    AlignerPyramide(base_pilotable, 0.0),
                    AllerPyramide(base_pilotable, 0.0, 1),

                ),
                Hold(troisdent)
            ),
            DropReset(troisdent)
        )