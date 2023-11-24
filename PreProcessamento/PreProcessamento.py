import cv2 as cv
imagem = cv.imread('./PreProcessamento/frutas.jpg')
valorPixel = imagem[150, 150]
print(valorPixel) #Retorna os valores do RGB da imagem


imagem = cv.cvtColor(imagem, cv.COLOR_RGB2GRAY) #Intensidade de luz representada por pixel em tons de cinza
valorPixel = imagem[150, 150]
print(valorPixel)

#Alterar o valor de um determinado pixel
imagem = cv.imread('./PreProcessamento/frutas.jpg')
print(imagem[150, 150]) #valor númérico referente ao pixel da linha 150 e da coluna 150
imagem[150, 150] = [255, 255, 255] #Setando o pixel agora equivalente a cor branca
print(imagem[150, 150])

#Saber o número de linhas , colunas e canais de uma imagem
imagem = cv.imread('./PreProcessamento/frutas.jpg')
print(imagem.shape) #No caso dessa imagem possui, 739 linhas, 704 colunas e 3 canais de cor
print(imagem.size) #Quantidade de pixels na imagem, no caso de a imagem ser colorida deve dividir pela quantidade de canais