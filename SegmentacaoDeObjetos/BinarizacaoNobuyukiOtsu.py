import cv2 as cv
import numpy as np

#Neste método o limiar é setado automaticamente 

imagemOriginal = cv.imread("./SegmentacaoDeObjetos/graos.jpg", 0)

tipo = cv.THRESH_BINARY_INV + cv.THRESH_OTSU
limiar, imagemBinarizada = cv.threshold(imagemOriginal, 0, 255, tipo)

print(limiar)
cv.imshow("Imagem Tratada", imagemBinarizada)
cv.imshow("Imagem Original", imagemOriginal)

cv.waitKey(0)
cv.destroyAllWindows()