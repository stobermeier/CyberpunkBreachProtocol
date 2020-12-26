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