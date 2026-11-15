import cv2
import os;
import pytesseract

def read_text_from_images(img_path: str) -> str:
    img = cv2.imread(f"img/{img_path}")
    
    return pytesseract.image_to_string(img)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

images = [f for f in os.listdir("img") if os.path.isfile(os.path.join("img", f))]

for img_path in images:
    print(img_path, "\t=>\t", read_text_from_images(img_path))

