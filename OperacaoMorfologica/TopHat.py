#TopHat Não muito usada
import cv2 as cv
import numpy as np

imagemOriginal = cv.imread("./OperacaoMorfologica/arroz.jpg", 0)

elementoEstruturante = cv.getStructuringElement(cv.MORPH_ELLIPSE, (25,25))
imagemProcessada = cv.morphologyEx(imagemOriginal, cv.MORPH_TOPHAT, elementoEstruturante)

#Ajuste de contraste 
imagemTratada = cv.add(imagemProcessada, imagemProcessada)
cv.imshow("Original", imagemOriginal)
cv.imshow("Resultado", imagemProcessada)
cv.imshow("Final", imagemTratada)

cv.waitKey(0)
cv.destroyAllWindows()