def main():
    n = int(input())

    dic = {}
    for _ in range(n):
        command = input().split(" ")
        value = command[1]
        if command[0] == 'insert':
            if value not in dic:
                dic[value] = 0
        elif command[0] == 'find':
            if value in dic:
                print('yes')
            else:
                print('no')
    return

if __name__ == '__main__':
    main()