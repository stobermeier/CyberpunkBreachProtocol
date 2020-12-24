import solver_backtracking
from solver import validate_hexdump, text_to_sequence, hexdump


def breach(hexdump, ram, datamine1, datamine2, datamine3):
    datamine1 = text_to_sequence(datamine1)
    datamine2 = text_to_sequence(datamine2)
    datamine3 = text_to_sequence(datamine3)

    # Check possible links between sequences
    _1_2 = datamine1[len(datamine1) - 1] == datamine2[0]
    _1_3 = datamine1[len(datamine1) - 1] == datamine3[0]
    _2_1 = datamine2[len(datamine2) - 1] == datamine1[0]
    _2_3 = datamine2[len(datamine2) - 1] == datamine3[0]
    _3_1 = datamine3[len(datamine3) - 1] == datamine1[0]
    _3_2 = datamine3[len(datamine3) - 1] == datamine2[0]

    sequences = []

    if (ram >= len(datamine3)):
        # Datamine 3 must be in the sequence
        # Can it be combined?
        if ram >= (len(datamine3) + len(datamine2) + len(datamine1) - 2):
            # 1_2_3
            if _1_2 and _2_3:
                sequences.append(datamine1 + datamine2[1:] + datamine3[1:])
            # 1_3_2
            if _1_3 and _3_2:
                sequences.append(datamine1 + datamine3[1:] + datamine2[1:])
            # 2_1_3
            if _2_1 and _1_3:
                sequences.append(datamine2 + datamine1[1:] + datamine3[1:])
            # 2_3_1
            if _2_3 and _3_1:
                sequences.append(datamine2 + datamine3[1:] + datamine1[1:])
            # 3_1_2
            if _3_1 and _1_2:
                sequences.append(datamine3 + datamine1[1:] + datamine2[1:])
            # 3_2_1
            if _3_2 and _2_1:
                sequences.append(datamine3 + datamine2[1:] + datamine1[1:])
        if ram >= (len(datamine3) + len(datamine2) - 1):
            # 2_3
            if _2_3:
                sequences.append(datamine2 + datamine3[1:])
            # 3_2
            if _3_2:
                sequences.append(datamine3 + datamine2[1:])

        sequences.append(datamine3)

    # Solve
    for seq in sequences:
        solver_backtracking.solve(hexdump, seq, ram)
        input('More? Following solutions will get worse.')


breach(hexdump, 12, '1CBD1C', '1CE97A7A', '7ABD1CE9')
