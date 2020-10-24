def add_matrix(mat1,mat2):
    result = []
    for i in range(len(A)):
        rows = []
        for j in range(len(A[0])):
           rows.append(A[i][j]+B[i][j])
            
        result.append(rows)
    print("Addition",result)

def multiple_matrix(mat1,mat2):
    result = [ [0,0,0],[0,0,0],[0,0,0]]
    for i in range (len(mat1)):
        
        for j in range(len(mat2[0])):
                       for k in range(len(mat2)):
                           result[i][j]+= A[i][j]* B[i][j]
    print("Multiplication",result)

def transpose(matrix):
    result=[ [0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i]=matrix[i][j]
    print("Transpose",result)

A = [[2,3,4],[4,2,1],[8,5,2]]
B = [[3,6,7],[7,2,3],[5,2,8]]
print("Matrix A",A)
print("Matrix B",B)
add_matrix(A,B)
transpose(A)
multiple_matrix(A,B)

               
