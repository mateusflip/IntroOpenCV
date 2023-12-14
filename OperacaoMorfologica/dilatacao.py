import cv2

imagemOriginal = cv2.imread("./OperacaoMorfologica/rolamento.jpg", 0)
elementoEstruturante = cv2.getStructuringElement(
  cv2.MORPH_ELLIPSE, (5,5)
)
imagemProcessada = cv2.dilate(
  imagemOriginal, elementoEstruturante, iterations = 5
)

cv2.imshow("Original", imagemOriginal)
cv2.imshow("Resultado", imagemProcessada)

cv2.waitKey(0)
cv2.destroyAllWindows()