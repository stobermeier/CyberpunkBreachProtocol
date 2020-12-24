import ocr_to_hexdump
import copy
import time


def validate_hexdump(hexdump):
    valid_hex = ['55', '7A', 'BD', '1C', 'E9']
    for col in hexdump:
        for row in col:
            if row not in valid_hex:
                print("Invalid Hex: {}".format(row))
                return -1


def text_to_sequence(text):
    seq = []
    for i in range(0, int(len(text) / 2)):
        seq.append(text[0:2])
        text = text[2:len(text)]
    return seq


def find_all_possible_combinations(hexdump, ram):
    all_possible_combinations = []

    hexdump_loc = copy.deepcopy(hexdump)

    for column in range(0, len(hexdump_loc)):
        hex_val = hexdump_loc[column][0]
        hexdump_loc[column][0] = '--'
        find_combination_recursive(all_possible_combinations, hexdump_loc, ram - 1, hex_val, str(column) + '0',
                                   [column, 0], 'vert')

    return all_possible_combinations


def find_combination_recursive(all_possible_combinations, hexdump_rec, ram_left, seq, seq_pos, last_position,
                               vert_horz):
    # print(seq)

    hexdump_loc = copy.deepcopy(hexdump_rec)
    hexdump_loc[last_position[0]][last_position[1]] = '--'

    if ram_left == 0:
        all_possible_combinations.append(seq + '--' + seq_pos)
        return

    if vert_horz == 'vert':
        column = last_position[0]
        for row in range(0, 6):
            if row != last_position[1] and hexdump_loc[column][row] != '--':
                find_combination_recursive(all_possible_combinations, hexdump_loc, ram_left - 1,
                                           seq + hexdump_loc[column][row], seq_pos + str(column) + str(row),
                                           [column, row], 'horz')
    elif vert_horz == 'horz':
        row = last_position[1]
        for column in range(0, 6):
            if column != last_position[0] and hexdump_loc[column][row] != '--':
                find_combination_recursive(all_possible_combinations, hexdump_loc, ram_left - 1,
                                           seq + hexdump_loc[column][row], seq_pos + str(column) + str(row),
                                           [column, row], 'vert')


def solve(hexdump, seq_text, ram):
    print("Validating Hexdump:")
    validate_hexdump(hexdump)
    print("Hexdump valid!")
    ram = int(ram)
    print("Attempt to solve:")
    ocr_to_hexdump.print_hexdump(hexdump)
    print("\nFind sequence {} with {} RAM".format(seq_text, ram))

    seq = text_to_sequence(seq_text)

    print(seq)
    if ram < len(seq):
        print("Insufficient RAM")
        return -1
    else:
        print("RAM could be sufficient")

    print("Calculate all possible sequences using {} RAM".format(ram))
    start = time.time()
    all_possible_combinations = find_all_possible_combinations(hexdump, ram)
    print("All possible sequences calculated!")
    print(time.time() - start)

    start = time.time()
    print("Trying to find Sequence {}".format(seq_text))
    for combination in all_possible_combinations:
        if combination.find(seq_text) != -1:
            print(text_to_sequence(combination))
            print(time.time() - start)
            return combination
    print(time.time() - start)
    return 'No solution could be found :('


hexdump = [['55', '1C', '55', 'BD', '1C', '7A'], ['7A', 'BD', '1C', '55', 'E9', '1C'],
           ['BD', '55', 'BD', '55', '55', '1C'], ['1C', '55', '1C', 'BD', '55', 'BD'],
           ['55', 'E9', '7A', '1C', '1C', '1C'], ['7A', 'BD', '1C', '55', '55', 'BD']]
'''
validate_hexdump(hexdump)
ocr_to_hexdump.print_hexdump(hexdump)

solve(hexdump, '7ABDE91C', 8)
'''
print("")
