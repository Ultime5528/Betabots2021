from pyfrc.physics.drivetrains import linear_deadzone
from pyfrc.physics.units import units
from wpimath.geometry import Rotation2d, Twist2d, Pose2d
from wpimath.kinematics import MecanumDriveKinematics, MecanumDriveWheelSpeeds, ChassisSpeeds, MecanumDriveOdometry


class MecanumDriveSim:
    def __init__(
        self,
        kinematics: MecanumDriveKinematics,
        deadzone: float = 0.01,
        speed: units.Quantity = 2 * units.mps,
    ):
        self.kinematics = kinematics
        self.speed = units.mps.m_from(speed, name="speed")
        self.speed_fl = 0.0
        self.speed_fr = 0.0
        self.speed_rl = 0.0
        self.speed_rr = 0.0
        self.position_fl = 0.0
        self.position_fr = 0.0
        self.position_rl = 0.0
        self.position_rr = 0.0
        self.deadzone = linear_deadzone(deadzone)
        self.wheelSpeeds = MecanumDriveWheelSpeeds()
        self.chassisSpeeds = ChassisSpeeds()
        self.pose = Pose2d()
        self.odometry = MecanumDriveOdometry(self.kinematics, Rotation2d.fromDegrees(0.0))
        self.angle_offset = Rotation2d()

    def update(self, input_fl, input_fr, input_rl, input_rr, dt=0.02):
        input_fl = self.deadzone(input_fl)
        input_fr = self.deadzone(input_fr)
        input_rl = self.deadzone(input_rl)
        input_rr = self.deadzone(input_rr)

        self.wheelSpeeds.frontLeft = input_fl * self.speed
        self.wheelSpeeds.frontRight = input_fr * self.speed
        self.wheelSpeeds.rearLeft = input_rl * self.speed
        self.wheelSpeeds.rearRight = input_rr * self.speed

        self.position_fl += self.wheelSpeeds.frontLeft * dt
        self.position_fr += self.wheelSpeeds.frontRight * dt
        self.position_rl += self.wheelSpeeds.rearLeft * dt
        self.position_rr += self.wheelSpeeds.rearRight * dt

        self.chassisSpeeds = self.kinematics.toChassisSpeeds(self.wheelSpeeds)
        twist = Twist2d(
            self.chassisSpeeds.vx * dt,
            self.chassisSpeeds.vy * dt,
            self.chassisSpeeds.omega * dt,
        )
        self.pose = self.pose.exp(twist)
        self.odometry.update(self.pose.rotation(), self.wheelSpeeds)

    def setPose(self, pose: Pose2d):
        self.pose = pose
        self.position_fl = 0.0
        self.position_fr = 0.0
        self.position_rl = 0.0
        self.position_rr = 0.0

    def getFrontLeftRate(self):
        return self.wheelSpeeds.frontLeft

    def getFrontRightRate(self):
        return self.wheelSpeeds.frontRight

    def getRearLeftRate(self):
        return self.wheelSpeeds.rearLeft

    def getRearRightRate(self):
        return self.wheelSpeeds.rearRight

    def getFrontLeftPosition(self):
        return self.position_fl

    def getFrontRightPosition(self):
        return self.position_fr

    def getRearLeftPosition(self):
        return self.position_rl

    def getRearRightPosition(self):
        return self.position_rr

    def getHeading(self):
        return self.pose.rotation()

    def resetOdometry(self):
        current_pose = self.odometry.getPose()
        # self.drive_sim.setPose(Pose2d())
        self.position_fl = 0.0
        self.position_fr = 0.0
        self.position_rl = 0.0
        self.position_rr = 0.0
        # self.angle_offset = current_pose.rotation().degrees()
        self.pose = Pose2d()
        self.odometry.resetPosition(current_pose, Rotation2d.fromDegrees(0.0))
