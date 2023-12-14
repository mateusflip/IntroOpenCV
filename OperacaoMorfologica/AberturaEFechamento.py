import cv2
import numpy as np

#Operação de Abertura
imagemOriginal = cv2.imread("./OperacaoMorfologica/rolamento3.jpg", 0)

elementoEstruturante = cv2.getStructuringElement(
  cv2.MORPH_ELLIPSE, (3,3)
)
imagemProcessada = cv2.morphologyEx(
  imagemOriginal, cv2.MORPH_OPEN, elementoEstruturante
)

cv2.imshow("Original", imagemOriginal)
cv2.imshow("Resultado", imagemProcessada)

cv2.waitKey(0)
cv2.destroyAllWindows()



#Operaçãod e fechamento
imagemOriginal = cv2.imread("./OperacaoMorfologica/rolamento4.jpg", 0)

elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))

imagemProcessada = cv2.morphologyEx(imagemOriginal, cv2.MORPH_CLOSE, elementoEstruturante)

cv2.imshow("Original Fechamento", imagemOriginal)
cv2.imshow("Resultado Fechamento", imagemProcessada)

cv2.waitKey(0)
cv2.destroyAllWindows()

#abertura e fechamento de tons cinzas (Pouco utilizada)
imagemOriginal = cv2.imread("./OperacaoMorfologica/arroz.jpg", 0)
elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_CROSS, (100, 100))
imagemProcessada = cv2.morphologyEx(imagemOriginal, cv2.MORPH_OPEN, elementoEstruturante)

imagemSubtraida = cv2.subtract(imagemOriginal, imagemProcessada)

# Ajusta de contraste da imagem
imagemTratada = cv2.add(imagemSubtraida, imagemSubtraida)


cv2.imshow("Original Tons de Cinza", imagemOriginal)
cv2.imshow("Resultado Tons de Cinza", imagemProcessada)
cv2.imshow("Subtraida Tons de Cinza", imagemSubtraida)
cv2.imshow("Tratada Tons de Cinza", imagemTratada)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Gradiente Morfológico
imagemOriginal = cv2.imread("./OperacaoMorfologica/rolamento4.jpg", 0)
elementoEstruturante = cv2.getStructuringElement(
  cv2.MORPH_ELLIPSE, (3,3)
)
imagemProcessada = cv2.morphologyEx(
  imagemOriginal, cv2.MORPH_GRADIENT, elementoEstruturante
)

cv2.imshow("Original Gradiente Morfológico", imagemOriginal)
cv2.imshow("Resultado Gradiente Morfológico", imagemProcessada)

cv2.waitKey(0)
cv2.destroyAllWindows()