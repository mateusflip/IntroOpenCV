import cv2

#Extraindo o canais de cores separados
imagem = cv2.imread('./RepresentacaoDeCoresNoEspaco4/Frutas.jpg')
if imagem is None:
    print("Could not read the image.")
azul, verde, vermelho = cv2.split(imagem)

cv2.imshow("Canal R", vermelho)
cv2.imshow("Canal G", verde)
cv2.imshow("Canal B", azul)

cv2.imwrite("./RepresentacaoDeCoresNoEspaco4/frutas-canal-vermelho.jpeg", vermelho)
cv2.imwrite("./RepresentacaoDeCoresNoEspaco4/frutas-canal-verde.jpeg", verde)
cv2.imwrite("./RepresentacaoDeCoresNoEspaco4/frutas-canal-azul.jpeg", azul)

cv2.waitKey(0)
cv2.destroyAllWindows()

#combinando os três canais em uma única imagem
imagem = cv2.merge((azul, verde, vermelho))
cv2.imshow("Imagem", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()

#convertendo a imagem em tons de cinza
imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
cv2.imshow("Imagem-Cinza", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()
