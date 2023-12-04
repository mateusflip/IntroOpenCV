import cv2 

imgOriginal = cv2.imread("./RealceDeBordas/estacionamento.jpg", 0)

imgTratada = cv2.Canny(imgOriginal, 100, 200) #Quanto maior forem os valores do segundo e terceiro parametro, menos bordas serão detectadas

cv2.imshow("Original", imgOriginal)
cv2.imshow("Tratada", imgTratada)

cv2.waitKey(0)
cv2.destroyAllWindows()