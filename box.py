num = int(input('Enter a Number: '))

for x in range (num):
    for y in range (num):
        if x == 0 or x == num - 1 or y == 0 or y == num - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()