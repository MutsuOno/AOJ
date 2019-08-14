input_line = input().split(" ")
a = int(input_line[0])
b = int(input_line[1])
print(" ".join([str(a*b)] + [str(a*2+b*2)]))