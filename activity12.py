import getpass

username = 'Hinata'
password = 'wanttobe_littlegiant'

us = input("Enter Username: ")
p = getpass.getpass("Enter Password: ")

if username == us and p == password :
    print('ACCESS GRANTED')

else : 
    print('ACCESS DENIED')
