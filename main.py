import cv2
import os;
import pytesseract

def read_text_from_images(img_path: str) -> str:
    img = cv2.imread(f"img/{img_path}")

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # converted_img = cv2.medianBlur(img, 3) # <- worse
    # converted_img = cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1] # lepiej trochę artefaktów
    converted_img = cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1] # odczytało jeden dodatkowy obreaz ale nie w pełni
    # converted_img = cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1] # odczytało 1.png idealnie, reszty niedoczytał
    # converted_img = cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2) # nic nie odczytało
    # converted_img = cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2) # nieczytelene
    # converted_img = cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2) # nieczytelne
    
    return pytesseract.image_to_string(converted_img)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

images = [f for f in os.listdir("img") if os.path.isfile(os.path.join("img", f))]

for img_path in images:
    print(img_path, "\t=>\t", read_text_from_images(img_path))

