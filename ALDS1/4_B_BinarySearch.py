import math

def binarySearch(A, n, key):
    left = 0
    right = n
    while left < right:
        mid = math.floor((left+right) / 2)
        if A[mid] == key:
            return True
        elif key < A[mid]:
            right = mid
        else:
            left = mid + 1
    return False

def main():
    n = int(input())
    S = [int(s) for s in input().split(" ")]
    _ = int(input())
    T = [int(s) for s in input().split(" ")]

    sum = 0

    for t in T:
        if binarySearch(S, n, t):
            sum += 1
    
    print(sum)

if __name__ == '__main__':
    main()