import math

import commands2
import wpilib
import wpilib.drive

import constants

class BasePilotable(commands2.SubsystemBase):

    # TBD
    pulses_per_meter = 1440.0

    def __init__(self) -> None:
        super().__init__()

        self.fl_motor = wpilib.VictorSP(constants.Ports.base_pilotable_moteur_fl)
        self.fr_motor = wpilib.VictorSP(constants.Ports.base_pilotable_moteur_fr)
        self.rl_motor = wpilib.VictorSP(constants.Ports.base_pilotable_moteur_rl)
        self.rr_motor = wpilib.VictorSP(constants.Ports.base_pilotable_moteur_rr)

        self.fl_motor_encoder = wpilib.Encoder(*constants.Ports.base_pilotable_encodeur_fl)
        self.fr_motor_encoder = wpilib.Encoder(*constants.Ports.base_pilotable_encodeur_fr)
        self.rl_motor_encoder = wpilib.Encoder(*constants.Ports.base_pilotable_encodeur_rl)
        self.rr_motor_encoder = wpilib.Encoder(*constants.Ports.base_pilotable_encodeur_rr)

        self.gyro = wpilib.AnalogGyro(constants.Ports.base_pilotable_gyro)

        self.drive = wpilib.drive.MecanumDrive(self.fl_motor, self.fr_motor, self.rl_motor,self.rr_motor)

        self.fl_motor_encoder.setDistancePerPulse(1 / self.pulses_per_meter)
        self.fr_motor_encoder.setDistancePerPulse(1 / self.pulses_per_meter)
        self.rl_motor_encoder.setDistancePerPulse(1 / self.pulses_per_meter)
        self.rr_motor_encoder.setDistancePerPulse(1 / self.pulses_per_meter)
        self.resetEncoders()

    def driveCartesian(self, ySpeed: float, xSpeed: float, zRot: float) -> None:
        self.drive.driveCartesian(ySpeed, xSpeed, zRot, self.gyro.getAngle())
    
    def drivePolar(self, mag: float, angle: float, zRot: float) -> None:
        self.drive.drivePolar(mag, angle, zRot)

    def resetEncoders(self) -> None:
        self.fl_motor_encoder.reset()
        self.fr_motor_encoder.reset()
        self.rl_motor_encoder.reset()
        self.rr_motor_encoder.reset()

    def resetGyro(self) -> None:
        self.gyro.reset()
