from getpass import getpass
uname = 'Power_shell'
pword = 'power_shell123'

isLogin = False

while isLogin == False:
    user = input('Enter Your Username: ')
    paword = getpass('Enter Your Password: ')

    if user == uname and paword == pword:
        print('LOGIN SUCCESS!')
        isLogin = True
    else:
        print('LOGIN FAILED!')
        isLogin = False