import sys, io, os, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Find latest screenshot
screenshot_dir = 'H:/截图'
files = []
for root, dirs, filenames in os.walk(screenshot_dir):
    for f in filenames:
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            files.append(os.path.join(root, f))

if not files:
    print('(没有找到截图)')
    sys.exit(0)

latest = max(files, key=os.path.getmtime)
print(f'=== {os.path.basename(latest)} ===')

img = Image.open(latest)
# Resize if too large for speed
w, h = img.size
if w * h > 4000000:  # >4MP
    scale = (4000000 / (w * h)) ** 0.5
    img = img.resize((int(w*scale), int(h*scale)))

text = pytesseract.image_to_string(img, lang='chi_sim+eng')
print(text if text.strip() else '(没有识别到文字)')
