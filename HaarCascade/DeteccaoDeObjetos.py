import numpy as np
import cv2 as cv

cascadeFace = cv.CascadeClassifier("./HaarCascade/frontalface.xml")
print("Arquivo cascade", cascadeFace)
imagemOriginal = cv.imread("./HaarCascade/roger.jpg")

imagem = cv.cvtColor(imagemOriginal, cv.COLOR_BGR2GRAY)

#image  	  Imagem em tons de cinza.  
#scaleFactor  	  Fator de escala para redução da imagem.  
#minNeighbors  	  Quantidade mínima de vizinhos.  
#minSize  	  Tamanho mínimo do retângulo que demarca o objeto. 

faces = cascadeFace.detectMultiScale(imagem, scaleFactor=1.3, minNeighbors=7, minSize=(30, 30))

#desenho do Retangulo nas faces detectadas
for(x,y,w,h) in faces:
    cv.rectangle(imagemOriginal, (x,y), (x+w, y+h), (000, 255, 0), 2)

#Exibindo o total de faces encontradas pelo algoritmo
print(len(faces))


cv.imshow("Resultado", imagemOriginal)
cv.waitKey(0)
cv.destroyAllWindows()
