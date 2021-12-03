import math

import commands2
import wpilib
import wpilib.drive
import rev
import navx

import constants


class BasePilotable(commands2.SubsystemBase):
    # TBD
    pulses_per_meter = 1.0
    use_navx = True

    def __init__(self) -> None:
        super().__init__()

        self.fl_motor = rev.CANSparkMax(constants.Ports.base_pilotable_moteur_fl, rev.MotorType.kBrushless)
        # self.fl_motor.restoreFactoryDefaults()
        # self.fl_motor.setInverted(False)
        # self.fl_motor.set
        self.fr_motor = rev.CANSparkMax(constants.Ports.base_pilotable_moteur_fr, rev.MotorType.kBrushless)
        # self.fr_motor.setInverted(True)
        # self.fl_motor.restoreFactoryDefaults()
        self.rl_motor = rev.CANSparkMax(constants.Ports.base_pilotable_moteur_rl, rev.MotorType.kBrushless)
        # self.rl_motor.setInverted(False)
        self.rr_motor = rev.CANSparkMax(constants.Ports.base_pilotable_moteur_rr, rev.MotorType.kBrushless)
        # self.rr_motor.setInverted(True)

        for controller in [self.fl_motor, self.fr_motor, self.rl_motor, self.rr_motor]:
            controller.restoreFactoryDefaults()
            # controller.setInverted(True)

        self.fr_motor.setInverted(True)
        self.rr_motor.setInverted(True)

        self.fl_motor_encoder = self.fl_motor.getEncoder()
        self.fr_motor_encoder = self.fr_motor.getEncoder()
        self.rl_motor_encoder = self.rl_motor.getEncoder()
        self.rr_motor_encoder = self.rr_motor.getEncoder()

        if self.use_navx:
            self.gyro = navx.AHRS(wpilib.SerialPort.Port.kMXP)
        else:
            self.gyro = wpilib.ADXRS450_Gyro()

        self.drive = wpilib.drive.MecanumDrive(self.fl_motor, self.rl_motor, self.fr_motor, self.rr_motor)
        self.drive.setRightSideInverted(False)

        self.fl_motor_encoder.setPositionConversionFactor(1 / self.pulses_per_meter)
        self.fr_motor_encoder.setPositionConversionFactor(1 / self.pulses_per_meter)
        self.rl_motor_encoder.setPositionConversionFactor(1 / self.pulses_per_meter)
        self.rr_motor_encoder.setPositionConversionFactor(1 / self.pulses_per_meter)
        self.resetOdometry()

    def driveCartesian(self, ySpeed: float, xSpeed: float, zRot: float) -> None:
        self.drive.driveCartesian(ySpeed, xSpeed, zRot, 0.0)
    
    def drivePolar(self, mag: float, angle: float, zRot: float) -> None:
        self.drive.drivePolar(mag, angle, zRot)

    def resetOdometry(self) -> None:
        self.fl_motor_encoder.setPosition(0)
        self.fr_motor_encoder.setPosition(0)
        self.rl_motor_encoder.setPosition(0)
        self.rr_motor_encoder.setPosition(0)
        self.gyro.reset()

    def periodic(self) -> None:
        wpilib.SmartDashboard.putNumber("fl_motor", self.fl_motor.get())
        wpilib.SmartDashboard.putNumber("fr_motor", self.fr_motor.get())
        wpilib.SmartDashboard.putNumber("rl_motor", self.rl_motor.get())
        wpilib.SmartDashboard.putNumber("rr_motor", self.rr_motor.get())

    def drive_test(self, value: float):
        self.fl_motor.set(value)
        self.fr_motor.set(value)
        self.rl_motor.set(value)
        self.rr_motor.set(value)
