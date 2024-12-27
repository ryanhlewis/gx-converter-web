class GCode:
    """Reading and preparation of gcode"""

    # Header:

    # ;test comment
    # ;start gcode
    # M118 X17.55 Y15.00 Z10.10 T0
    # M140 S50 T0
    # M104 S222 T0
    # M104 S0 T1
    # M107
    # G90
    # G28
    # M132 X Y Z A B
    # G1 Z50.000 F420
    # G161 X Y F3300
    # M7 T0
    # M6 T0
    # M651 S255

    # Footer:

    # ;end gcode
    # M104 S0 T0
    # M140 S0 T0
    # G162 Z F1800
    # G28 X Y
    # M132 X Y A B
    # M652
    # G91
    # M18
