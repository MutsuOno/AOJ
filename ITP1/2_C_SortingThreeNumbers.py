input_line = list(map(int, input().split()))
input_line = sorted(input_line)
for i in input_line:
    if i == input_line[len(input_line)-1]:
        print(i)
    else:
        print(i, end=" ")