import cv2 as cv
import numpy as np

#Melhor utilizada quando se possui uma iluminação desfavorável na imagem

imagemOriginal = cv.imread("./SegmentacaoDeObjetos/comprimidos.jpg", 0)
imagemTratada = cv.medianBlur(imagemOriginal, 7)

imagemBinarizada = cv.adaptiveThreshold(imagemTratada, 255,
                                        cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv.THRESH_BINARY_INV, 11, 5)

cv.imshow("Imagem Original", imagemOriginal)
cv.imshow("Imagem Tratada", imagemBinarizada)

cv.waitKey(0)
cv.destroyAllWindows()