def satitize_rows(rows):
    new_rows = []
    for r in rows:
        if len(r) < 12:
            r += '0' * (12 - len(r))
        elif len(r) > 12:
            r = r[0:12]
        new_rows.append(r)
    return new_rows


def rows_to_hexdump(rows):
    hexdump = [[], [], [], [], [], []]
    for row in rows:
        # print("Processing row: " + row)
        for column in range(0, 6):
            hex = row[0:2]
            # print("Placing: " + hex)
            hexdump[column].append(hex)
            row = row[2:len(row)]
    return hexdump


def print_hexdump(hexdump):
    for row in range(0, 6):
        print('{} {} {} {} {} {}'.format(hexdump[0][row], hexdump[1][row], hexdump[2][row], hexdump[3][row],
                                         hexdump[4][row], hexdump[5][row]))


def convert_ocr_to_hexdump(ocr_text):
    rows = ocr_text.splitlines()
    rows = satitize_rows(rows[0:6])
    hexdump = rows_to_hexdump(rows)
    return [rows, hexdump]


def convert_rows_to_hexdump(rows):
    rows = satitize_rows(rows[0:6])
    hexdump = rows_to_hexdump(rows)
    return [rows, hexdump]
