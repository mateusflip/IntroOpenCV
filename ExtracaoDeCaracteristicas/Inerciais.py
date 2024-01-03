import cv2
import numpy as np

imagem = cv2.imread("./ExtracaoDeCaracteristicas/quadrado.jpg", 0)
momentos = cv2.moments(imagem)

print(momentos)