for j in range(6, 0, -1):
    for e in range(1, j + 1):
        print(' ', end=' ')
    for m in range(1, 7 - j):
        print(m, end=' ')
    for a in range(5 - j, 0, -1):
        print(a, end=' ')
    print()
