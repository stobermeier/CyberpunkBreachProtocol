try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    hexdump_img = Image.open(filename)

    custom_config = r'-c tessedit_char_whitelist=557ABD1CE9 --psm 6'
    # custom_config = r'--oem 0 --psm 6'
    # custom_config = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 6'

    text = pytesseract.image_to_string(hexdump_img,
                                       config=custom_config)  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text
