from math import hypot
from typing import List
import commands2
from termcolor import colored
from wpimath.trajectory import TrajectoryConfig, TrajectoryGenerator
from wpilib.geometry import Pose2d, Translation2d
from subsystems.basepilotable import BasePilotable
from commands.specific_turn import SpecificTurn
from commands.drive_distance import DriveDistance

class SuivreTrajectoire(commands2.CommandBase):
    def __init__(self, drive: BasePilotable, waypoints: List[Pose2d], maxVelocity: float, maxAcceleration: float) -> None:
        super().__init__()
        self.drive = drive
        self.trajectory = TrajectoryGenerator.generateTrajectory(
             
            waypoints, 
             
            TrajectoryConfig(maxAcceleration, maxVelocity))
        self.states = self.trajectory.states()

        with open("traj.csv", "w+") as f:
            for state in self.states:
                f.write(f"{state.pose.X()};{state.pose.Y()};{state.pose.rotation().degrees()}\n".replace(".", ","))

        self.angleInitial = self.trajectory.states()[0].pose.rotation()
    
    def initialize(self) -> None:
        self.drive.resetOdometry()
        self.index = 0

    def execute(self) -> None:
        while(self.index < len(self.states) and self.drive.odometry.getPose().translation().distance(self.states[self.index].pose.translation()) <= 0.25):
            self.index += 1

        # self.error = self.trajectory.states()[self.index].pose.rotation() - self.drive.gyro.getAngle() - self.angleInitial
        # print(colored(self.states, 'green'))
        twistPath = self.drive.odometry.getPose().log(self.states[self.index].pose)
        hypotenuse = hypot(twistPath.dx, twistPath.dy)

        print(colored(self.drive.odometry.getPose().translation().distance(self.states[self.index].pose.translation()), "green"))
        print(twistPath.dx/hypotenuse)
        print(colored(twistPath.dtheta_degrees, "red"))
        
        self.drive.driveCartesian(twistPath.dy/hypotenuse, twistPath.dx/hypotenuse, twistPath.dtheta_degrees)

    def isFinished(self) -> bool:
        return self.index > len(self.states)

    def end(self, interrupted: bool) -> None:
        self.drive.driveCartesian(0, 0, 0)

        