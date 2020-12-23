try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2


def ocr_core(hexdump_img):
    """
    This function will handle the core OCR processing of images.
    """
    # hexdump_img = Image.open(filename)

    custom_config = r'-c tessedit_char_whitelist=557ABD1CE9 --psm 6'
    # custom_config = r'--oem 0 --psm 6'
    # custom_config = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 6'

    text = pytesseract.image_to_string(hexdump_img,
                                       config=custom_config)  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text


filename = "images\\hexdump.png"

'''
img = cv2.imread(filename)
# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def remove_noise(image):
    return cv2.medianBlur(image, 1)


def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


img = get_grayscale(img)
img = remove_noise(img)
img = thresholding(img)
# cv2.imshow('image', img)
cv2.waitKey(0)
'''

img = Image.open(filename)
text = ocr_core(img)
rows = text.splitlines()


# rows = ['BD1C7A5555E9', 'BD17A5555E9', 'BD1C555E9', 'BD1DC7A555C5E9']


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


rows = satitize_rows(rows[0:6])
hexdump = rows_to_hexdump(rows)

print("\nSolution:")
print_hexdump(hexdump)
