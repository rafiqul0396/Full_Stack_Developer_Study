# given a matrix with  N*N elements, print the elements of the matrix in column wise order


def print_matrix(matrix):
    n=len(matrix)
    m=len(matrix[0])
    for j in range(m):
        for i in range(n):
            print(matrix[i][j], end=" ")
            
        print()





# drive  code

if __name__ == "__main__":
    matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print_matrix(matrix)
    




'''
# main
n=int(input())
matrix=[]
for i in range(n):
    row=[int(x) for x in input().split()]
    matrix.append(row)                                                      

print_matrix(matrix)
'''
    


# Sample Input:         
# 3
# 1 2 3
# 4 5 6
# 7 8 9

