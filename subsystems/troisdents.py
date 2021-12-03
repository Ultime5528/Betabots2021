import wpilib
import commands2

from constants import Ports

class TroisDents(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        wpilib.SendableRegistry.getInstance().addLW(
            self,
            self.__class__.__name__,
            self.__class__.__name__)

        self.piston = wpilib.DoubleSolenoid(*Ports.trois_dents_piston)
        self.addChild("Piston", self.piston)

    def drop(self):
        self.piston.set(wpilib.DoubleSolenoid.Value.kReverse)

    def take(self):
        self.piston.set(wpilib.DoubleSolenoid.Value.kForward)

    def idle(self):
        self.piston.set(wpilib.DoubleSolenoid.Value.kOff)

