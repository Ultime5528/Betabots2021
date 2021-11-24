import wpilib
import commands2


class TroisDents(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        wpilib.SendableRegistry.getInstance().addLW(
            self,
            self.__class__.__name__,
            self.__class__.__name__)

        self.piston = wpilib.DoubleSolenoid(0, 1)
        self.addChild("Piston", self.piston)

    def drop(self):
        self.piston.set(wpilib.DoubleSolenoid.Value.kForward)

    def take(self):
        self.piston.set(wpilib.DoubleSolenoid.Value.kReverse)

    def idle(self):
        self.piston.set(wpilib.DoubleSolenoid.Value.kOff)
