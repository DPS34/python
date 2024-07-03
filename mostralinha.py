def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [2, 3, 1]
valores = [10, 30, 60, 0, 20, 90]
dobra(valores)
print(valores)