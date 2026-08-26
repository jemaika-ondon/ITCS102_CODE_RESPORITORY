money = 14568

a = money//1000
money = money % 1000
b = money//500
money = money % 500
c = money//200
money = money % 200
d = money//100
money = money % 100
e = money//50 
money = money % 50
f = money//20
money = money % 20
g = money//10
money = money % 10
h = money//5
money = money % 5
i = money//1
money = money % 1

print("\n\t\t\tMoney to Deposit -->",money)
print("\n\t\t\t1000 -",a)
print("\t\t\t500 -",b)
print("\t\t\t200 -",c)
print("\t\t\t100 -",d)
print("\t\t\t50 -",e)
print("\t\t\t20 -",f)
print("\t\t\t10 -",g)
print("\t\t\t5 -",h)
print("\t\t\t1 -",i)