from PIL import Image
import pytesseract

def extract_text_from_image(img_path):
    try:
        img = Image.open(img_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Error to read file {e}")
        return None

img_path = input("Input image path: ")
string = extract_text_from_image(img_path)
print(f"String after extract: {string}")
