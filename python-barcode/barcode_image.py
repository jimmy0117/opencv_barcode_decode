"""
Read Barcode image
"""
import pyzbar.pyzbar as pyzbar
from PIL import Image

image = "test.jpg"

# 開啟檔案
img = Image.open(image)

# 顯示
img.show()

# 解碼
barcodes = pyzbar.decode(img)

# 轉成utf-8
for barcode in barcodes:
    barcodeData = barcode.data.decode("utf-8")
    print(barcodeData)