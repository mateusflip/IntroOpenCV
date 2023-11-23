import cv2

#o espaço de cor HSV é o model ideal a ser utilizado para segmentar objetos coloridos

imagem = cv2.imread('./RepresentacaoDeCoresNoEspaco4/Frutas.jpg')
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
matiz, saturacao, valor = cv2.split(imagem)

cv2.imshow("Canal H", matiz)
cv2.imshow("Canal S", saturacao)
cv2.imshow("Canal V", valor)

cv2.waitKey(0)
cv2.destroyAllWindows()

#combinando os canais de uma imagem HSV
imagem = cv2.merge((matiz, saturacao, valor))
imagem = cv2.cvtColor(imagem, cv2.COLOR_HSV2BGR)
cv2.imshow("IMAGEM HSV", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()