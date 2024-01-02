import cv2 as cv
import numpy as np

imgRGB = cv.imread("./SegmentacaoDeObjetos/cubo-magico.jpg", 0)

imgHSV = cv.cvtColor(imgRGB, cv.COLOR_BGR2HSV)

tomClaro = np.array([160, 100, 100])
tomEscuro = np.array([200, 255, 255])

imgSegmentada = cv.inRange(imgHSV, tomClaro, tomEscuro)

cv.imshow("Original", imgRGB) 
cv.imshow("Segmentada", imgSegmentada)

cv.waitKey(0)
cv.destroyAllWindows()