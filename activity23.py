#anime concept
shonen = []
korea = []
isekai = []
adventure = []
fantasy = []

while True:
    ans = input('Do You Watch or read any anime?  yes/no: ').lower()

    if ans == 'yes':
        print('What Kind of Anime do you Watch or read? ')
        print('1 Shonen \n2 Korean \n3 Isekai \n4 Adventure \n5 Fantasy')

        choice = int('Input:   ')

        if choice == 1 :
            print('Shonen')
            title = input('Please input the Title of the ANIME:    ')
            shonen.append('title')
            print('List of Shonen')
            print(shonen)
            con = input('Do you wish to continue yes / no  ').lower()
            if con == 'yes':
                continue
            else:
                break
        else:
            print('INVALID choice')