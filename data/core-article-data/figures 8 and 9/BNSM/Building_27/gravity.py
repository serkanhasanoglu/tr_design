import openseespy.opensees as ops


def do_gravity() -> None:
    """Perform linear static analysis under gravity loads.
    """
    # Add gravity time-series and load pattern to ops domain
    ops.timeSeries('Constant', 1)
    ops.pattern('Plain', 1, 1)

    # Add beam gravity loads to ops domain
    ops.eleLoad('-ele', 1017, '-type', '-beamUniform', -26.35564356, 0.0)
    ops.eleLoad('-ele', 1018, '-type', '-beamUniform', -3.96, 0.0)
    ops.eleLoad('-ele', 1019, '-type', '-beamUniform', -26.35564356, 0.0)
    ops.eleLoad('-ele', 1020, '-type', '-beamUniform', -35.11128713, 0.0)
    ops.eleLoad('-ele', 1021, '-type', '-beamUniform', -22.245, 0.0)
    ops.eleLoad('-ele', 1022, '-type', '-beamUniform', -35.11128713, 0.0)
    ops.eleLoad('-ele', 1023, '-type', '-beamUniform', -35.11128713, 0.0)
    ops.eleLoad('-ele', 1024, '-type', '-beamUniform', -11.57, 0.0)
    ops.eleLoad('-ele', 1025, '-type', '-beamUniform', -35.11128713, 0.0)
    ops.eleLoad('-ele', 1026, '-type', '-beamUniform', -26.35564356, 0.0)
    ops.eleLoad('-ele', 1027, '-type', '-beamUniform', -14.585, 0.0)
    ops.eleLoad('-ele', 1028, '-type', '-beamUniform', -26.35564356, 0.0)
    ops.eleLoad('-ele', 2017, '-type', '-beamUniform', -26.35564356, 0.0)
    ops.eleLoad('-ele', 2018, '-type', '-beamUniform', -3.96, 0.0)
    ops.eleLoad('-ele', 2019, '-type', '-beamUniform', -26.35564356, 0.0)
    ops.eleLoad('-ele', 2020, '-type', '-beamUniform', -35.11128713, 0.0)
    ops.eleLoad('-ele', 2021, '-type', '-beamUniform', -22.245, 0.0)
    ops.eleLoad('-ele', 2022, '-type', '-beamUniform', -35.11128713, 0.0)
    ops.eleLoad('-ele', 2023, '-type', '-beamUniform', -35.11128713, 0.0)
    ops.eleLoad('-ele', 2024, '-type', '-beamUniform', -11.57, 0.0)
    ops.eleLoad('-ele', 2025, '-type', '-beamUniform', -35.11128713, 0.0)
    ops.eleLoad('-ele', 2026, '-type', '-beamUniform', -26.35564356, 0.0)
    ops.eleLoad('-ele', 2027, '-type', '-beamUniform', -14.585, 0.0)
    ops.eleLoad('-ele', 2028, '-type', '-beamUniform', -26.35564356, 0.0)
    ops.eleLoad('-ele', 3017, '-type', '-beamUniform', -26.35564356, 0.0)
    ops.eleLoad('-ele', 3018, '-type', '-beamUniform', -3.96, 0.0)
    ops.eleLoad('-ele', 3019, '-type', '-beamUniform', -26.35564356, 0.0)
    ops.eleLoad('-ele', 3020, '-type', '-beamUniform', -35.11128713, 0.0)
    ops.eleLoad('-ele', 3021, '-type', '-beamUniform', -22.245, 0.0)
    ops.eleLoad('-ele', 3022, '-type', '-beamUniform', -35.11128713, 0.0)
    ops.eleLoad('-ele', 3023, '-type', '-beamUniform', -35.11128713, 0.0)
    ops.eleLoad('-ele', 3024, '-type', '-beamUniform', -11.57, 0.0)
    ops.eleLoad('-ele', 3025, '-type', '-beamUniform', -35.11128713, 0.0)
    ops.eleLoad('-ele', 3026, '-type', '-beamUniform', -26.35564356, 0.0)
    ops.eleLoad('-ele', 3027, '-type', '-beamUniform', -14.585, 0.0)
    ops.eleLoad('-ele', 3028, '-type', '-beamUniform', -26.35564356, 0.0)
    ops.eleLoad('-ele', 4017, '-type', '-beamUniform', -16.30574257, 0.0)
    ops.eleLoad('-ele', 4018, '-type', '-beamUniform', -2.4, 0.0)
    ops.eleLoad('-ele', 4019, '-type', '-beamUniform', -16.30574257, 0.0)
    ops.eleLoad('-ele', 4020, '-type', '-beamUniform', -31.41148515, 0.0)
    ops.eleLoad('-ele', 4021, '-type', '-beamUniform', -21.09, 0.0)
    ops.eleLoad('-ele', 4022, '-type', '-beamUniform', -31.41148515, 0.0)
    ops.eleLoad('-ele', 4023, '-type', '-beamUniform', -31.41148515, 0.0)
    ops.eleLoad('-ele', 4024, '-type', '-beamUniform', -9.98, 0.0)
    ops.eleLoad('-ele', 4025, '-type', '-beamUniform', -31.41148515, 0.0)
    ops.eleLoad('-ele', 4026, '-type', '-beamUniform', -16.30574257, 0.0)
    ops.eleLoad('-ele', 4027, '-type', '-beamUniform', -5.59, 0.0)
    ops.eleLoad('-ele', 4028, '-type', '-beamUniform', -16.30574257, 0.0)
    ops.eleLoad('-ele', 4045, '-type', '-beamUniform', -19.72, 0.0)
    ops.eleLoad('-ele', 4050, '-type', '-beamUniform', -19.72, 0.0)
    ops.eleLoad('-ele', 4055, '-type', '-beamUniform', -19.72, 0.0)
    ops.eleLoad('-ele', 4060, '-type', '-beamUniform', -19.72, 0.0)
    ops.eleLoad('-ele', 1029, '-type', '-beamUniform', -16.22, 0.0)
    ops.eleLoad('-ele', 1030, '-type', '-beamUniform', -16.82, 0.0)
    ops.eleLoad('-ele', 1031, '-type', '-beamUniform', -16.82, 0.0)
    ops.eleLoad('-ele', 1032, '-type', '-beamUniform', -16.22, 0.0)
    ops.eleLoad('-ele', 1033, '-type', '-beamUniform', -16.22, 0.0)
    ops.eleLoad('-ele', 1034, '-type', '-beamUniform', -19.54159091, 0.0)
    ops.eleLoad('-ele', 1035, '-type', '-beamUniform', -19.54159091, 0.0)
    ops.eleLoad('-ele', 1036, '-type', '-beamUniform', -16.22, 0.0)
    ops.eleLoad('-ele', 1037, '-type', '-beamUniform', -16.22, 0.0)
    ops.eleLoad('-ele', 1038, '-type', '-beamUniform', -19.54159091, 0.0)
    ops.eleLoad('-ele', 1039, '-type', '-beamUniform', -19.54159091, 0.0)
    ops.eleLoad('-ele', 1040, '-type', '-beamUniform', -16.22, 0.0)
    ops.eleLoad('-ele', 2029, '-type', '-beamUniform', -16.22, 0.0)
    ops.eleLoad('-ele', 2030, '-type', '-beamUniform', -16.82, 0.0)
    ops.eleLoad('-ele', 2031, '-type', '-beamUniform', -16.82, 0.0)
    ops.eleLoad('-ele', 2032, '-type', '-beamUniform', -16.22, 0.0)
    ops.eleLoad('-ele', 2033, '-type', '-beamUniform', -16.22, 0.0)
    ops.eleLoad('-ele', 2034, '-type', '-beamUniform', -19.54159091, 0.0)
    ops.eleLoad('-ele', 2035, '-type', '-beamUniform', -19.54159091, 0.0)
    ops.eleLoad('-ele', 2036, '-type', '-beamUniform', -16.22, 0.0)
    ops.eleLoad('-ele', 2037, '-type', '-beamUniform', -16.22, 0.0)
    ops.eleLoad('-ele', 2038, '-type', '-beamUniform', -19.54159091, 0.0)
    ops.eleLoad('-ele', 2039, '-type', '-beamUniform', -19.54159091, 0.0)
    ops.eleLoad('-ele', 2040, '-type', '-beamUniform', -16.22, 0.0)
    ops.eleLoad('-ele', 3029, '-type', '-beamUniform', -16.22, 0.0)
    ops.eleLoad('-ele', 3030, '-type', '-beamUniform', -16.52, 0.0)
    ops.eleLoad('-ele', 3031, '-type', '-beamUniform', -16.52, 0.0)
    ops.eleLoad('-ele', 3032, '-type', '-beamUniform', -16.22, 0.0)
    ops.eleLoad('-ele', 3033, '-type', '-beamUniform', -16.22, 0.0)
    ops.eleLoad('-ele', 3034, '-type', '-beamUniform', -19.24159091, 0.0)
    ops.eleLoad('-ele', 3035, '-type', '-beamUniform', -19.24159091, 0.0)
    ops.eleLoad('-ele', 3036, '-type', '-beamUniform', -16.22, 0.0)
    ops.eleLoad('-ele', 3037, '-type', '-beamUniform', -16.22, 0.0)
    ops.eleLoad('-ele', 3038, '-type', '-beamUniform', -19.24159091, 0.0)
    ops.eleLoad('-ele', 3039, '-type', '-beamUniform', -19.24159091, 0.0)
    ops.eleLoad('-ele', 3040, '-type', '-beamUniform', -16.22, 0.0)
    ops.eleLoad('-ele', 4029, '-type', '-beamUniform', -7.6, 0.0)
    ops.eleLoad('-ele', 4030, '-type', '-beamUniform', -8.56, 0.0)
    ops.eleLoad('-ele', 4031, '-type', '-beamUniform', -8.56, 0.0)
    ops.eleLoad('-ele', 4032, '-type', '-beamUniform', -7.6, 0.0)
    ops.eleLoad('-ele', 4033, '-type', '-beamUniform', -7.6, 0.0)
    ops.eleLoad('-ele', 4034, '-type', '-beamUniform', -17.115, 0.0)
    ops.eleLoad('-ele', 4035, '-type', '-beamUniform', -17.115, 0.0)
    ops.eleLoad('-ele', 4036, '-type', '-beamUniform', -7.6, 0.0)
    ops.eleLoad('-ele', 4037, '-type', '-beamUniform', -7.6, 0.0)
    ops.eleLoad('-ele', 4038, '-type', '-beamUniform', -17.115, 0.0)
    ops.eleLoad('-ele', 4039, '-type', '-beamUniform', -17.115, 0.0)
    ops.eleLoad('-ele', 4040, '-type', '-beamUniform', -7.6, 0.0)

    # Add column gravity loads to ops domain
    ops.load(170001, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(121001, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(170004, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(121004, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(170005, 0.0, 0.0, -6.804, 0.0, 0.0, 0.0)
    ops.load(121005, 0.0, 0.0, -6.804, 0.0, 0.0, 0.0)
    ops.load(170006, 0.0, 0.0, -8.4, 0.0, 0.0, 0.0)
    ops.load(121006, 0.0, 0.0, -8.4, 0.0, 0.0, 0.0)
    ops.load(170007, 0.0, 0.0, -8.4, 0.0, 0.0, 0.0)
    ops.load(121007, 0.0, 0.0, -8.4, 0.0, 0.0, 0.0)
    ops.load(170008, 0.0, 0.0, -6.804, 0.0, 0.0, 0.0)
    ops.load(121008, 0.0, 0.0, -6.804, 0.0, 0.0, 0.0)
    ops.load(170009, 0.0, 0.0, -6.804, 0.0, 0.0, 0.0)
    ops.load(121009, 0.0, 0.0, -6.804, 0.0, 0.0, 0.0)
    ops.load(170010, 0.0, 0.0, -8.4, 0.0, 0.0, 0.0)
    ops.load(121010, 0.0, 0.0, -8.4, 0.0, 0.0, 0.0)
    ops.load(170011, 0.0, 0.0, -8.4, 0.0, 0.0, 0.0)
    ops.load(121011, 0.0, 0.0, -8.4, 0.0, 0.0, 0.0)
    ops.load(170012, 0.0, 0.0, -6.804, 0.0, 0.0, 0.0)
    ops.load(121012, 0.0, 0.0, -6.804, 0.0, 0.0, 0.0)
    ops.load(170013, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(121013, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(170014, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(121014, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(170015, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(121015, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(170016, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(121016, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(171001, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(122001, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(171004, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(122004, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(171005, 0.0, 0.0, -6.804, 0.0, 0.0, 0.0)
    ops.load(122005, 0.0, 0.0, -6.804, 0.0, 0.0, 0.0)
    ops.load(171006, 0.0, 0.0, -8.4, 0.0, 0.0, 0.0)
    ops.load(122006, 0.0, 0.0, -8.4, 0.0, 0.0, 0.0)
    ops.load(171007, 0.0, 0.0, -8.4, 0.0, 0.0, 0.0)
    ops.load(122007, 0.0, 0.0, -8.4, 0.0, 0.0, 0.0)
    ops.load(171008, 0.0, 0.0, -6.804, 0.0, 0.0, 0.0)
    ops.load(122008, 0.0, 0.0, -6.804, 0.0, 0.0, 0.0)
    ops.load(171009, 0.0, 0.0, -6.804, 0.0, 0.0, 0.0)
    ops.load(122009, 0.0, 0.0, -6.804, 0.0, 0.0, 0.0)
    ops.load(171010, 0.0, 0.0, -8.4, 0.0, 0.0, 0.0)
    ops.load(122010, 0.0, 0.0, -8.4, 0.0, 0.0, 0.0)
    ops.load(171011, 0.0, 0.0, -8.4, 0.0, 0.0, 0.0)
    ops.load(122011, 0.0, 0.0, -8.4, 0.0, 0.0, 0.0)
    ops.load(171012, 0.0, 0.0, -6.804, 0.0, 0.0, 0.0)
    ops.load(122012, 0.0, 0.0, -6.804, 0.0, 0.0, 0.0)
    ops.load(171013, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(122013, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(171014, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(122014, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(171015, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(122015, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(171016, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(122016, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(172001, 0.0, 0.0, -2.1, 0.0, 0.0, 0.0)
    ops.load(123001, 0.0, 0.0, -2.1, 0.0, 0.0, 0.0)
    ops.load(172004, 0.0, 0.0, -2.1, 0.0, 0.0, 0.0)
    ops.load(123004, 0.0, 0.0, -2.1, 0.0, 0.0, 0.0)
    ops.load(172005, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(123005, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(172006, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(123006, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(172007, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(123007, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(172008, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(123008, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(172009, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(123009, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(172010, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(123010, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(172011, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(123011, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(172012, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(123012, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(172013, 0.0, 0.0, -2.1, 0.0, 0.0, 0.0)
    ops.load(123013, 0.0, 0.0, -2.1, 0.0, 0.0, 0.0)
    ops.load(172014, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(123014, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(172015, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(123015, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(172016, 0.0, 0.0, -2.1, 0.0, 0.0, 0.0)
    ops.load(123016, 0.0, 0.0, -2.1, 0.0, 0.0, 0.0)
    ops.load(173001, 0.0, 0.0, -2.1, 0.0, 0.0, 0.0)
    ops.load(124001, 0.0, 0.0, -2.1, 0.0, 0.0, 0.0)
    ops.load(173004, 0.0, 0.0, -2.1, 0.0, 0.0, 0.0)
    ops.load(124004, 0.0, 0.0, -2.1, 0.0, 0.0, 0.0)
    ops.load(173005, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(124005, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(173006, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(124006, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(173007, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(124007, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(173008, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(124008, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(173009, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(124009, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(173010, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(124010, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(173011, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(124011, 0.0, 0.0, -5.376, 0.0, 0.0, 0.0)
    ops.load(173012, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(124012, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(173013, 0.0, 0.0, -2.1, 0.0, 0.0, 0.0)
    ops.load(124013, 0.0, 0.0, -2.1, 0.0, 0.0, 0.0)
    ops.load(173014, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(124014, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(173015, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(124015, 0.0, 0.0, -4.116, 0.0, 0.0, 0.0)
    ops.load(173016, 0.0, 0.0, -2.1, 0.0, 0.0, 0.0)
    ops.load(124016, 0.0, 0.0, -2.1, 0.0, 0.0, 0.0)
    ops.load(170002, 0.0, 0.0, -2.688, 0.0, 0.0, 0.0)
    ops.load(124017, 0.0, 0.0, -2.688, 0.0, 0.0, 0.0)
    ops.load(174017, 0.0, 0.0, -2.688, 0.0, 0.0, 0.0)
    ops.load(121002, 0.0, 0.0, -2.688, 0.0, 0.0, 0.0)
    ops.load(170003, 0.0, 0.0, -2.688, 0.0, 0.0, 0.0)
    ops.load(124018, 0.0, 0.0, -2.688, 0.0, 0.0, 0.0)
    ops.load(174018, 0.0, 0.0, -2.688, 0.0, 0.0, 0.0)
    ops.load(121003, 0.0, 0.0, -2.688, 0.0, 0.0, 0.0)
    ops.load(171002, 0.0, 0.0, -2.688, 0.0, 0.0, 0.0)
    ops.load(124019, 0.0, 0.0, -2.688, 0.0, 0.0, 0.0)
    ops.load(174019, 0.0, 0.0, -2.688, 0.0, 0.0, 0.0)
    ops.load(122002, 0.0, 0.0, -2.688, 0.0, 0.0, 0.0)
    ops.load(171003, 0.0, 0.0, -2.688, 0.0, 0.0, 0.0)
    ops.load(124020, 0.0, 0.0, -2.688, 0.0, 0.0, 0.0)
    ops.load(174020, 0.0, 0.0, -2.688, 0.0, 0.0, 0.0)
    ops.load(122003, 0.0, 0.0, -2.688, 0.0, 0.0, 0.0)
    ops.load(172002, 0.0, 0.0, -2.058, 0.0, 0.0, 0.0)
    ops.load(124021, 0.0, 0.0, -2.058, 0.0, 0.0, 0.0)
    ops.load(174021, 0.0, 0.0, -2.058, 0.0, 0.0, 0.0)
    ops.load(123002, 0.0, 0.0, -2.058, 0.0, 0.0, 0.0)
    ops.load(172003, 0.0, 0.0, -2.058, 0.0, 0.0, 0.0)
    ops.load(124022, 0.0, 0.0, -2.058, 0.0, 0.0, 0.0)
    ops.load(174022, 0.0, 0.0, -2.058, 0.0, 0.0, 0.0)
    ops.load(123003, 0.0, 0.0, -2.058, 0.0, 0.0, 0.0)
    ops.load(173002, 0.0, 0.0, -2.058, 0.0, 0.0, 0.0)
    ops.load(124023, 0.0, 0.0, -2.058, 0.0, 0.0, 0.0)
    ops.load(174023, 0.0, 0.0, -2.058, 0.0, 0.0, 0.0)
    ops.load(124002, 0.0, 0.0, -2.058, 0.0, 0.0, 0.0)
    ops.load(173003, 0.0, 0.0, -2.058, 0.0, 0.0, 0.0)
    ops.load(124024, 0.0, 0.0, -2.058, 0.0, 0.0, 0.0)
    ops.load(174024, 0.0, 0.0, -2.058, 0.0, 0.0, 0.0)
    ops.load(124003, 0.0, 0.0, -2.058, 0.0, 0.0, 0.0)

    # Perform gravity analysis and save the model state
    ops.system('UmfPack')
    ops.numberer('RCM')
    ops.constraints('Transformation')
    ops.test('NormDispIncr', 1e-08, 1)
    ops.integrator('LoadControl', 1)
    ops.algorithm('Linear')
    ops.analysis('Static')
    ops.analyze(1)
    ops.loadConst('-time', 0.0)
    ops.wipeAnalysis()
