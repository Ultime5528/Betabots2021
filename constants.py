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
    pilotage_max_x = ntproperty("/Proprietes/PilotageMaxX", 0.4, writeDefault=False)
    pilotage_max_y = ntproperty("/Proprietes/PilotageMaxY", 0.4, writeDefault=False)
    pilotage_max_z = ntproperty("/Proprietes/PilotageMaxZ", 0.2, writeDefault=False)
    pilotage_deadzone = ntproperty("/Proprietes/PilotageDeadzone", 0.05, writeDefault=False)
    aligner_max_speed = ntproperty("/Proprietes/AlignerMaxSpeed", 0.15, writeDefault=False)
    aligner_error_multiplier = ntproperty("/Proprietes/AlignerErrorMultiplier", 1.5, writeDefault=False)
    aller_max_speed = ntproperty("/Proprietes/AllerMaxSpeed", 0.05, writeDefault=False)

Proprietes = _Proprietes()
