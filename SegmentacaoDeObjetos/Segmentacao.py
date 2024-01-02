#Segmentação por Binarização
import cv2 as cv
import numpy as np

imgOriginal = cv.imread("./SegmentacaoDeObjetos/graos.jpg", 0)

#Processo de Binarização
metodo = cv.THRESH_BINARY_INV #Mantém os objetos de interesse na cor branca
ret, imgBinarizada = cv.threshold(imgOriginal, 135, 255, metodo) #segundo parametro é valor de limiar(Geralmente tentativa e erro), terceiro valor da intensidade que receberá os pixels

#Operação de fechamento
elementoEstruturante = cv.getStructuringElement(cv.MORPH_CROSS, (3,3))
imagemProcessada = cv.morphologyEx(imgBinarizada, cv.MORPH_CLOSE, elementoEstruturante)

#aplicando Erosão
imagemErosaoFinal = cv.erode(imagemProcessada, elementoEstruturante, iterations = 1)



cv.imshow("Imagem Original", imgOriginal)
cv.imshow("Imagem Tratada", imgBinarizada)
cv.imshow("Imagem Tratada Com fechamento", imagemProcessada)
cv.imshow("Imagem Tratada com Erosão final", imagemErosaoFinal)

cv.waitKey(0)
cv.destroyAllWindows()