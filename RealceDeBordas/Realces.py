import cv2 

imagem = cv2.imread("./RealceDeBordas/estacionamento.jpg", 0)
imgTratada = cv2.Laplacian(imagem, cv2.IPL_DEPTH_8U)
imgRealcada = cv2.subtract(imagem, imgTratada)

cv2.imshow("Original", imagem)
cv2.imshow("Tratada", imgTratada)
cv2.imshow("Realçada", imgRealcada)

cv2.waitKey(0)
cv2.destroyAllWindows()