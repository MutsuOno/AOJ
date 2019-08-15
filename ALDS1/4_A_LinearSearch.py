def linearSearch(A, n, key):
    i = 0
    A.append(key)
    while A[i] != key:
        i += 1
        if i == n:
            return False
    return True

def main():
    n = int(input())
    S = input().split(" ")
    _ = int(input())
    T = input().split(" ")

    sum = 0

    for s in T:
        if linearSearch(S, n, s):
            sum += 1
    
    print(sum)

if __name__ == '__main__':
    main()