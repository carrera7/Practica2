nombres = "'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David', 'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Facundo', 'FEDERICO', 'FEDERICO', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Jonathan', 'Jorge', 'JOSE', 'JUAN', 'Juan', 'Juan', 'Julian', 'Julieta', 'LAUTARO', 'Leonel', 'LUIS', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás', 'NICOLÁS', 'Noelia', 'Pablo', 'Priscila', 'TOMAS', 'Tomás', 'Ulises','Yanina'"
notas1 = "81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74"
notas2 = "30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37, 64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73, 95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10"

nombres = nombres.replace("'","")
nombres = nombres.replace(",","")
notas1 = notas1.replace(",","")
notas2 = notas2.replace(",","")
lista_nombres = nombres.split()
lista_notas1 = notas1.split()
lista_notas2 = notas2.split()

dicci = {}
for indice in range (len(lista_nombres)):
    dicci[lista_nombres[indice]] = int(lista_notas1[indice]) + int (lista_notas2[indice])
dicci

suma = 0
for elem in dicci:
    suma = dicci[elem] + suma
print (suma)

promedio = suma / len(dicci)
print (promedio)

for indice in dicci:
    if(dicci[indice] < promedio):
        print(indice)