sum = 0 
tuloy = True

while tuloy == True:
    x = int(input('Enter a Number: '))

    if x == 0:
        print('LOOP TERMINATED')
        print('TOTAL OF ALL NUMBER: ',sum)
        break

    else: 
        print('CONTINUE LOOP')
        sum += x 
        print('CURRENT TOTAL: ',sum)
        continue