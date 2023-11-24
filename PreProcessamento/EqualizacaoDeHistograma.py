import cv2 as cv 
import numpy as np
from matplotlib import pyplot as grafico

imagemOriginal = cv.imread("./PreProcessamento/maquina.jpg", 0)
imagemEqualizada = cv.equalizeHist(imagemOriginal)

cv.imshow("imagem Original", imagemOriginal)
cv.imshow("imagem Equalizada", imagemEqualizada)

grafico.hist(imagemOriginal.ravel(), 256, [0,256])
grafico.title('Original')
grafico.figure()
grafico.hist(imagemEqualizada.ravel(), 256, [0,256])
grafico.title("Equalizado")

grafico.show()

##Alterar a proporção de uma imagem
imagemModificada = cv.resize(
    imagemOriginal, None, fx = 0.5, fy = 0.5,
    interpolation = cv.INTER_CUBIC
)

cv.imshow("Resultado", imagemModificada)

cv.waitKey(0)
cv.destroyAllWindows()