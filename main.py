import cv2

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

for i in range(2):
    img = cv2.imread(f'img/img{i}.png')

    print(pytesseract.image_to_string(img))