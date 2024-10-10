#estructura bidimensional

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print (matrix[1][1])
#de esta manera se recorre una matris linea por linea 

def print_matrix (matrix):
    for row in matrix: #-> recorre filas
        for element in row:#-> recorre columnas
            print(element, end=" | ")
        print("\n")    

# como imprimir solo lo que necesito 

print(matrix[1][1], matrix[2][0])



matrix_1= [ [1,2],[3,4]]
matrix_2= [[5,6],[7,8]]

#suma = [[6,8],[10.12]]
suma = [[0,0],[0,0]]

for i in range (len(matrix_1)):
    for j in range (len(matrix_2)):
        suma[i][j]= matrix_1[i][j]+ matrix_2 [i][j]


print_matrix(suma)        