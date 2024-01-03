import cv2 as cv
import statistics

imagemBinaria = cv.imread("./ExtracaoDeCaracteristicas/tampaBinaria.jpg", 0)
imagemCinza = cv.imread("./ExtracaoDeCaracteristicas/tampaCinza.jpg", 0)
imagemRGB = cv.imread("./ExtracaoDeCaracteristicas/tampaRGB.jpg", 0)

rolBinaria = imagemBinaria.ravel() # retorna a cor predominante de pixel da imagem
rolCinza = imagemCinza.ravel()

print(statistics.mode(rolBinaria)) #Retorna predominante branca
print(statistics.mode(rolCinza)) 

valorMedioRGB = cv.mean(imagemRGB)
valorMedioCinza = cv.mean(imagemCinza)

print(valorMedioRGB)
print(valorMedioCinza)