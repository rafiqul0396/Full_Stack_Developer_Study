# print the matrix in  row wise order
def print_matrix(matrix):
    n=len(matrix)
    m=len(matrix[0])
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=" ")
        print()


# Driver code
if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_matrix(matrix)

# Output:
1 2 3
4 5 6
7 8 9
