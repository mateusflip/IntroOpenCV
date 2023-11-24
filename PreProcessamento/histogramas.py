import cv2 as cv
import numpy as np
from matplotlib import pyplot as grafico

#Histograma de imagem preto e branco
imagem = cv.imread('./PreProcessamento/folhasBinarias.bmp', 0)
grafico.hist(imagem.ravel(), 256, [0,256]) #Parametros = Imagem que vamos trabalhar, número de elementos, escala de elementos de 0(preto) a 255(branco)
grafico.show()

#Histograma de imagem cinza
imagem = cv.imread('./PreProcessamento/folhaCinza.png', 0)
grafico.hist(imagem.ravel(), 256, [0,256]) #Parametros = Imagem que vamos trabalhar, número de elementos, escala de elementos de 0(preto) a 255(branco)
grafico.show()

#Histogramas de imagens Coloridas
imagem = cv.imread('./PreProcessamento/folhaColorida.bmp')
azul, verde, vermelho = cv.split(imagem)
grafico.hist(azul.ravel(), 256, [0,256]) #Parametros = Imagem que vamos trabalhar, número de elementos, escala de elementos de 0(preto) a 255(branco)
grafico.figure()

grafico.hist(verde.ravel(), 256, [0,256])
grafico.figure()

grafico.hist(vermelho.ravel(), 256, [0, 256])
grafico.show()

#OBSERVAÇÃO = Imagens muito expostas a luz tendem a ter o gráfico par a direita, Já com menos luz para a esquerda