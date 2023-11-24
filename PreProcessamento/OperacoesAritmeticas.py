import cv2 as cv

imagemFichasVermelhas = cv.imread('./PreProcessamento/fichasVermelhas.bmp')
imagemFichasPretas = cv.imread('./PreProcessamento/fichasPretas.bmp')

#Adicionando duas imagens
imagem = cv.add(imagemFichasVermelhas, imagemFichasPretas)

cv.imshow("Resultado", imagem)
cv.waitKey(0)
cv.destroyAllWindows()


#Remoção
ficha1 = cv.imread('./PreProcessamento/fichaPos1.bmp')
ficha2 = cv.imread('./PreProcessamento/fichaPos2.bmp')

imagem = cv.subtract(ficha1, ficha2)
cv.imshow("Resultado Subtração", imagem)

cv.waitKey(0)
cv.destroyAllWindows()