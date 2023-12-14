import cv2 as cv
import pandas as pd

imagemOriginal = cv.imread("./OperacaoMorfologica/engrenagem.jpg",0)
elementoEstruturante = cv.getStructuringElement(cv.MORPH_CROSS, (3,3)) #remove a granulação da imagem original
imagemProcessada = cv.erode(imagemOriginal, elementoEstruturante,iterations=1) #ajusta a imagem e quantidade de interações do elemento estruturante

cv.imshow("Original", imagemOriginal)
cv.imshow("Resultado", imagemProcessada)

cv.waitKey(0)
cv.destroyAllWindows()