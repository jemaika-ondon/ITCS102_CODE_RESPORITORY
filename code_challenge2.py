money = int(input('Enter amount --> '))

k = money//1000
money = money % 1000
five_h = money//500
money = money % 500
two_h = money//200
money = money % 200
one_h = money//100
money = money % 100
fives = money//50 
money = money % 50
twos = money//20
money = money % 20
ten = money//10
money = money % 10
five = money//5
money = money % 5
one = money//1
money = money % 1

print("\n\t\t\tMoney to Deposit -->",money)
print("\n\t\t\t1000 -",k)
print("\t\t\t500 -",five_h)
print("\t\t\t200 -",two_h)
print("\t\t\t100 -",one_h)
print("\t\t\t50 -",fives)
print("\t\t\t20 -",twos)
print("\t\t\t10 -",ten)
print("\t\t\t5 -",five)
print("\t\t\t1 -",one)