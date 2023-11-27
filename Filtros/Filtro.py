import cv2 as cv

#filtro de media
imgOriginal = cv.imread("./Filtros/moedas.png")
imgTratada = cv.blur(imgOriginal, (5,5))

cv.imshow("Oginal", imgOriginal)
cv.imshow("Tratada", imgTratada)

cv.waitKey(0)
cv.destroyAllWindows()

#Filtro Gausiano
imgGaussianaTratada = cv.GaussianBlur(imgOriginal, (5,5), 0)
cv.imshow("Tratada Gaussiana", imgGaussianaTratada)
cv.waitKey(0)
cv.destroyAllWindows()

#Filtro mediana
imgMediana = cv.medianBlur(imgOriginal,5)
cv.imshow("Mediana tratada", imgMediana)
cv.waitKey(0)
cv.destroyAllWindows()

#Filtro Bilateral (O mais indicado para preservar bordas e contornos)
imgBilateral = cv.bilateralFilter(imgOriginal, 9, 75, 75)
cv.imshow("Bilateral tratada", imgBilateral)
cv.waitKey(0)
cv.destroyAllWindows()