import cv2
import numpy as np

cap1 = cv2.imread("./SegmentacaoDeObjetos/captura1.jpg", 0)
cap2 = cv2.imread("./SegmentacaoDeObjetos/captura2.jpg", 0)

imgRGB = cv2.subtract(cap1, cap2)
imgHSV = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2HSV)

tomClaro = np.array([0, 120, 120])
tomEscuro = np.array([180, 255, 255])

imgSegmentada = cv2.inRange(imgHSV, tomClaro, tomEscuro)
cv2.imshow("Segmentada", imgSegmentada)

cv2.waitKey(0)
cv2.destroyAllWindows()