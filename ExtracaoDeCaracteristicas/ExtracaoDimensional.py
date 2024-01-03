import cv2
import numpy as np

imagem = cv2.imread("./ExtracaoDeCaracteristicas/quadrado.jpg", 0)
tipo = cv2.THRESH_BINARY
ret, imgBinarizada = cv2.threshold(imagem, 127, 255, tipo)

# Obtendo os contornos dos objetos na imagem
modo = cv2.RETR_TREE;
metodo = cv2.CHAIN_APPROX_SIMPLE;
contornos, hierarquia = cv2.findContours(
    imgBinarizada, modo, metodo
)

# Obtendo os contornos do primeiro objeto segmentado
objeto = contornos[0]

# Obtendo a área do objeto segmentado
area = cv2.contourArea(objeto)
print(area)

perimetro = cv2.arcLength(objeto, True)
print("O perimetro e ", perimetro)