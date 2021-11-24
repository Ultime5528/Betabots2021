import math

import commands2
import wpilib
import wpilib.drive
import rev

import constants

class BasePilotable(commands2.SubsystemBase):

    # TBD
    pulses_per_meter = 1440.0

    def __init__(self) -> None:
        super().__init__()

        self.fl_motor = rev.CANSparkMax(constants.Ports.base_pilotable_moteur_fl, rev.CANSparkMaxLowLevel.MotorType.kBrushless)
        self.fr_motor = rev.CANSparkMax(constants.Ports.base_pilotable_moteur_fr, rev.CANSparkMaxLowLevel.MotorType.kBrushless)
        self.rl_motor = rev.CANSparkMax(constants.Ports.base_pilotable_moteur_rl, rev.CANSparkMaxLowLevel.MotorType.kBrushless)
        self.rr_motor = rev.CANSparkMax(constants.Ports.base_pilotable_moteur_rr, rev.CANSparkMaxLowLevel.MotorType.kBrushless)

        self.fl_motor_encoder = self.fl_motor.getEncoder()
        self.fr_motor_encoder = self.fr_motor.getEncoder()
        self.rl_motor_encoder = self.rl_motor.getEncoder()
        self.rr_motor_encoder = self.rr_motor.getEncoder()

        self.gyro = wpilib.ADXRS450_Gyro()

        self.drive = wpilib.drive.MecanumDrive(self.fl_motor, self.fr_motor, self.rl_motor,self.rr_motor)

        self.fl_motor_encoder.setPositionConversionFactor(1 / self.pulses_per_meter)
        self.fr_motor_encoder.setPositionConversionFactor(1 / self.pulses_per_meter)
        self.rl_motor_encoder.setPositionConversionFactor(1 / self.pulses_per_meter)
        self.rr_motor_encoder.setPositionConversionFactor(1 / self.pulses_per_meter)
        self.resetOdometry()

    def driveCartesian(self, ySpeed: float, xSpeed: float, zRot: float) -> None:
        self.drive.driveCartesian(ySpeed, xSpeed, zRot, self.gyro.getAngle())
    
    def drivePolar(self, mag: float, angle: float, zRot: float) -> None:
        self.drive.drivePolar(mag, angle, zRot)

    def resetOdometry(self) -> None:
        self.fl_motor_encoder.setPosition(0)
        self.fr_motor_encoder.setPosition(0)
        self.rl_motor_encoder.setPosition(0)
        self.rr_motor_encoder.setPosition(0)
        self.gyro.reset()

    
    def getAverageEncoderDistance(self) -> float:
        return (self.fl_motor_encoder.getDistance() + 
            self.fr_motor_encoder.getDistance() + 
            self.rl_motor_encoder.getDistance() + 
            self.rr_motor_encoder.getDistance()) / 4 
