from sklearn.neighbors import KNeighborsClassifier

caracteristicas = [
[3.10,  11.98,  14.68,  16.86, -32.64,  22.85,  33.25],
[3.11,  12.36,  14.63,  17.06,  32.99,  23.34,  33.16],
[3.07,  12.26,  14.62,  15.32,  31.40, -22.69, -30.30],
[3.10,  11.98,  14.68,  16.86, -32.64,  22.85,  33.25],
[3.11,  12.36,  14.63,  17.06,  32.99,  23.34,  33.16],
[3.07,  12.26,  14.62,  15.32,  31.40, -22.69, -30.30],
[3.12,  11.72,  14.76,  15.33,  32.08,  21.40,  30.37],
[3.14,  11.78,  14.83,  15.59, -34.29,  21.71,  30.81],
[3.13,  10.43,  14.77,  15.44,  31.55,  20.75,  30.54],
[3.12,  11.72,  14.76,  15.33,  32.08,  21.40,  30.37],
[3.14,  11.78,  14.83,  15.59, -34.29,  21.71,  30.81],
[3.13,  10.43,  14.77,  15.44,  31.55,  20.75,  30.54]
]

classificacoes = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

knn = KNeighborsClassifier(3) #Procurando os três valores mais próximos do que desejamos encontrar, sempre bom que seja um valor ímpar para evitar empate

knn.fit(caracteristicas, classificacoes)
objetoDesconhecido = [[3.17, 11.84, 14.91, 16.22, -33.21, 22.38, 31.78]]
resultado = knn.predict(objetoDesconhecido)

print(knn.score(caracteristicas, classificacoes)) #Podemos dizer que um algoritmo é tipo com boa acertividade caso o resultado seja maior que 0.8

print("A classe do objeto é ", resultado)

objetos = [
[3.17, 11.84, 14.91, 16.22, -33.21, 22.38, 31.78],
[3.17, 11.82, 14.91, 16.21, -33.38, 22.33, 31.77]
]

print("Nvos objetos ", knn.predict(objetos))