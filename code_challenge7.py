num = int(input('Enter a number:  '))

for j in range(num):
    for s in range(num - j - 1):
        print(" ", end=" ")
    for e in range(2 * j + 1):
        print("* ", end=" ")
    print()

# Lower half
for j in range(num - 2, -1, -1):
    for s in range(num - j - 1):
        print(" ", end=" ")
    for e in range(2 * j + 1):
        print("* ", end=" ")
    print()