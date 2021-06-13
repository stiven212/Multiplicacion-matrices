matriz1, matriz2 = [], []

print("Ingrese dimensiones de la matriz1")

row1 = int(input("Numero de filas "))
col1 = int(input("Numero de columnas "))

print("Ingrese dimensiones de la matriz2")

row2 = int(input("Numero de filas "))
col2 = int(input("Numero de columnas "))


if(col1 != row2):

    print('Valores no validos para multiplicación')
else:
    print('Complete la matriz1')
    for i in range(row1):
        array1 = []
        for j in range(col1):
            array1.append(
                int(input("Ingrese el valor en la posición (%d,%d) " % (i, j))))

        matriz1.append(array1)

    print("Matriz 1")
    for i in range(row1):

        print(matriz1[i])

    print('Complete la matriz2')
    for i in range(row2):
        array2 = []
        for j in range(col2):
            array2.append(
                int(input("Ingrese el valor en la posición (%d,%d) " % (i, j))))

        matriz2.append(array2)

    print("Matriz 2")
    for k in range(row2):

        print(matriz2[k])

    matriz3 = []
    for i in range(row1):
        array3 = []
        for j in range(col2):
            array3.append(0)

        matriz3.append(array3)


for i in range(len(matriz1)):
    for j in range(len(matriz2[0])):
        for k in range(len(matriz2)):
            matriz3[i][j] += (matriz1[i][k]*matriz2[k][j])

print("Matriz resultado")
for i in range(0, row1):
    print(matriz3[i])


""" print(matriz2)


print("Matriz 1")
for i in range(col1):
    for j in range(row1):
        matriz1[i][j] = int(
            input("Ingrese el valor en la posición: (%d,%d)" % (i, j)))

print("Matriz 2")
for i in range(col2):
    for j in range(row2):
        matriz2[i][j] = int(
            input("Ingrese el valor en la posición: (%d,%d)" % (i, j)))
 """
