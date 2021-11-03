import wpilib.simulation

from pyfrc.physics.core import PhysicsInterface
from pyfrc.physics import drivetrains

class PhysicsEngine:

    def __init__(self, physics_controller: PhysicsInterface):
        self.physics_controller = physics_controller

        self.fl_motor = wpilib.simulation.PWMSim(0)
        self.fr_motor = wpilib.simulation.PWMSim(1)
        self.rl_motor = wpilib.simulation.PWMSim(2)
        self.rr_motor = wpilib.simulation.PWMSim(3)

        self.gyro = wpilib.simulation.AnalogGyroSim(1)

        self.drivetrain = drivetrains.MecanumDrivetrain()

    def update_sim(self, now: float, tm_diff: float) -> None:
        fl_motor = self.fl_motor.getSpeed()
        fr_motor = self.fr_motor.getSpeed()
        rl_motor = self.rl_motor.getSpeed()
        rr_motor = self.rr_motor.getSpeed()

        speeds = self.drivetrain.calculate(fl_motor, fr_motor, rl_motor, rr_motor)
        pose = self.physics_controller.drive(speeds, tm_diff)

        self.gyro.setAngle(-pose.rotation().degrees())
