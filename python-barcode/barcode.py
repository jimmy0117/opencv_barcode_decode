""" 流程
1. 匯入套件
2. 設定視窗
3. 開啟攝影機
4. 讀取影像並解碼與顯示
5. 釋放相機
6. 刪除視窗
"""
# 匯入cv2, pyzbar
import cv2
import pyzbar.pyzbar as pyzbar

# 設定視窗
cv2.namedWindow("camera",cv2.WINDOW_NORMAL)

# 開啟攝影機
camera = cv2.VideoCapture(0)

#讀取影像並解碼顯示
while True:
    # 讀取當前image frame
    ret, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
    # 照片解碼
    barcodes = pyzbar.decode(gray)

    # 照片裡可能有數個條碼
    for barcode in barcodes:
        # 轉換解碼資料成utf-8的模式
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # 列印條形碼資料和條形碼型別
        print("掃描結果==》 類別： {0} 內容： {1}".format(barcodeType, barcodeData))
    # 顯示動態影像
    cv2.imshow("camera", frame)    
    # 按下ESC退出
    if(cv2.waitKey(5)==27):
        break
# 釋放相機
camera.release()
# 刪除視窗
cv2.destroyAllWindows()