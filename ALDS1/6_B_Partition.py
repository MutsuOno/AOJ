def partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    
    return i

def main():
    n = int(input())
    A = [int(x) for x in input().split()]

    q = partition(A, 0, n-1)

    left = A[:q+1]
    p = A[q+1]
    right = A[q+2:]
    print('{0} [{1}] {2}'.format(' '.join(map(str, left)), p, ' '.join(map(str, right))))
             
if __name__ == "__main__":
    main()