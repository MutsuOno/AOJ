input_line = input().split(" ")
W = int(input_line[0])
H = int(input_line[1])
x = int(input_line[2])
y = int(input_line[3])
r = int(input_line[4])

if x-r >= 0 and x+r <= W and y-r >= 0 and y+r <= H:
    print("Yes")
else:
    print("No")