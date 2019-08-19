import sys
input = sys.stdin.readline

def solve(A, i, n, m):
    if m == 0:
        return True
    if i >= n:
        return False
    return solve(A, i + 1, n, m) or solve(A, i + 1, n, m - A[i])

def main():
    n = int(input())
    A = list(map(int, input().split()))

    _ = int(input())
    m_list = list(map(int, input().split()))
    sum_list = sum(A)

    for m in m_list:
        if sum_list < m:
            print("no")
        elif solve(A, 0, n, m):
            print("yes")
        else:
            print("no")

if __name__ == '__main__':
    main()