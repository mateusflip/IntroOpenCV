import cv2 as cv
import numpy as np

imgOriginal = cv.imread("./SegmentacaoDeObjetos/graos.jpg", 0)

metodo = cv.THRESH_BINARY
ret, imagemBinarizada = cv.threshold(imgOriginal, 135, 255, metodo)

e = np.ones((3,3), np.uint8)
imagemTratada = cv.morphologyEx(imagemBinarizada, cv.MORPH_CLOSE, e)
imagemTratada = cv.erode(imagemTratada, e, iterations=2)

imagemSegmentada = cv.Canny(imagemTratada, 100, 200)

cv.imshow("Binarizada", imagemBinarizada)
cv.imshow("Tratada", imagemTratada)
cv.imshow("Segmentada", imagemSegmentada)

cv.waitKey(0)
cv.destroyAllWindows()