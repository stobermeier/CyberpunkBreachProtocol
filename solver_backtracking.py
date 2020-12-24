from solver_helper import validate_hexdump, text_to_sequence
import copy
import numpy as np


def guide(seq_pos):
    hd = [['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-']]

    seq_pos = text_to_sequence(seq_pos)

    for step in range(len(seq_pos)):
        column = seq_pos[step][0:1]
        row = seq_pos[step][1:2]
        hd[int(column)][int(row)] = str(step)

    print(np.array(hd).T)


def possible_start_points(hexdump, hex_val):
    start_points = []
    for column in range(6):
        for row in range(6):
            if hexdump[column][row] == hex_val:
                start_points.append((column, row))
    return start_points


def find_combination(hexdump, ram, start_point, sequence):
    hd = copy.deepcopy(hexdump)

    hex_val = sequence[0]
    column = start_point[0]
    row = start_point[1]

    if start_point[1] == 0:
        # Start in first row
        hd[column][row] = '--'
        find_combination_recursive(hd, ram - 1, hex_val, str(column) + str(row), (column, row), 'vert', sequence[1:])
    else:
        # Reach first element from first row
        seq = hd[column][0] + hd[column][row]
        seq_pos = str(column) + '0' + str(column) + str(row)
        hd[column][0] = '--'
        hd[column][row] = '--'
        find_combination_recursive(hd, ram - 2, seq, seq_pos, (column, row), 'horz', sequence[1:])


def find_combination_recursive(hd_, ram_left, seq, seq_pos, last_position, vert_horz, remaining_sequence):
    hd = copy.deepcopy(hd_)
    rs = copy.deepcopy(remaining_sequence)

    if not rs:
        print(text_to_sequence(seq))
        print(text_to_sequence(seq_pos))
        guide(seq_pos)
        input('Next')
        return

    if ram_left < 1:
        return

    if vert_horz == 'vert':
        column = last_position[0]
        for row in range(6):
            if row != last_position[1] and hd[column][row] == rs[0]:
                hex_val = hd[column][row]
                hd[column][row] = '--'
                find_combination_recursive(hd, ram_left - 1, seq + hex_val, seq_pos + str(column) + str(row),
                                           (column, row), 'horz', rs[1:])
        return

    elif vert_horz == 'horz':
        row = last_position[1]
        for column in range(6):
            if column != last_position[0] and hd[column][row] == rs[0]:
                hex_val = hd[column][row]
                hd[column][row] = '--'
                find_combination_recursive(hd, ram_left - 1, seq + hex_val, seq_pos + str(column) + str(row),
                                           (column, row), 'vert', rs[1:])
        return


def solve(hexdump, seq, ram):
    print("Validating Hexdump:")
    validate_hexdump(hexdump)
    print("Hexdump valid!")
    ram = int(ram)
    print("Attempt to solve:")
    print(np.array(hexdump).T)
    print("\nFind sequence {} with {} RAM".format(seq, ram))

    print(seq)
    if ram < len(seq):
        print("Insufficient RAM")
        return -1
    else:
        print("RAM could be sufficient")

    start_points = possible_start_points(hexdump, seq[0])
    for sp in start_points:
        find_combination(hexdump, ram, sp, seq)
