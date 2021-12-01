from typing import List
import commands2
from wpimath.trajectory import TrajectoryConfig, TrajectoryGenerator
from wpilib.geometry import Pose2d, Translation2d
from subsystems.basepilotable import BasePilotable

class SuivreTrajectoire(commands2.CommandBase):
    def __init__(self, drive: BasePilotable, positionDebut: Pose2d, waypoints: List[Translation2d], positionFin: Pose2d, maxVelocity: float, maxAcceleration: float) -> None:
        super().__init__()
        self.drive = drive
        self.trajectory = TrajectoryGenerator.generateTrajectory(
            positionDebut, 
            waypoints, 
            positionFin, 
            TrajectoryConfig(maxAcceleration, maxVelocity))
        self.angleInitial = self.trajectory.states()[0].pose.rotation()
    
    def initialize(self) -> None:
        self.drive.resetOdometry()
        self.index = 0

    def execute(self) -> None:
        while(self.index > len(self.trajectory.states())):
            self.index += 1

        self.error = self.trajectory.states()[self.index].pose.rotation() - self.drive.gyro.getAngle() - self.angleInitial