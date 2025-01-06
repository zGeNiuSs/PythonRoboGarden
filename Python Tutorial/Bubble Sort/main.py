ls = [1, 9, 4, 7, 2, 5, 8, 3]
idx = 0

while idx < len(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            temp = ls[i + 1]
            ls[i + 1] = ls[i]
            ls[i] = temp
    idx += 1

print(ls)