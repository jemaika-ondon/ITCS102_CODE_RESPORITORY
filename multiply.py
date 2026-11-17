col = int(input('Enter number of a Column:  '))

for j in range(1,11):
    for m in range(1, col + 1):
        print(j, 'x', m, '=', j*m, end='\t')
    print()