# given a matrix  of n*n size, find the row with maximum sum

def max_rowSum(matrix):
    # n is the number of rows
    n=len(matrix)
    # m is the number of columns
    m=len(matrix[0])
    #max_sum is the maximum sum of the row
    max_sum=0
    # max_row is the row with maximum sum
    max_row=0
    # iterate over each row
    for i in range(n):
        sum=0
        # sum of each row
        for j in range(m):
            sum+=matrix[i][j]
        # if sum is greater than max_sum, update max_sum and max_row
        if sum>max_sum:
            max_sum=sum
            max_row=i
    return max_row

# Driver code
if __name__ == '__main__':
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    print(max_rowSum(matrix))
