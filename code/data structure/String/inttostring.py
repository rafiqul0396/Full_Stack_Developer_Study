class Solution:
    def reverse(x: int) -> int:
        A=x
        A=str(A)
        b=A[::-1]
        b=b.strip()
        print(b)
        
        return int(b)#int(float(A))


if __name__ == "__main__":
    print(Solution.reverse(123))