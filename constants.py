from networktables.util import ntproperty


class Ports:
    # PWM
    base_pilotable_moteur_fl = 1
    base_pilotable_moteur_fr = 2
    base_pilotable_moteur_rl = 4
    base_pilotable_moteur_rr = 3

    # Gyro
    base_pilotable_gyro = 0

    # PCM
    trois_dents_piston = (0, 1)


class _Proprietes:
    dropReturnTime = ntproperty("/Proprietes/Trois Dents/DropReturnTime", 1, writeDefault=False)
    dropResetTime = ntproperty("/Proprietes/Trois Dents/DropResetTime", 1, writeDefault=False)
    mode_pilotage = ntproperty("/Proprietes/ModePilotage/selected", "A", writeDefault=False)


Proprietes = _Proprietes()
