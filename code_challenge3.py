# Problem: Global Freight Calculator  

sender_name = input('Enter Your Name: ')
type_of_item = input('Enter Your Item: ') 
is_Fragile = bool(input('Is it FRAGILE? '))
weight = eval(input('Your Items Weight?' ))
distance = eval(input('Gaano Kalayo?' ))
is_express = bool(input('Nagmamadali kaba? '))
is_international = bool(input('International ba? '))

base_cost = (weight * 2.50) + (distance * 0.15)

#print(base_cost)
#print(sender_name )
#print(type_of_item)
#print(is_Fragile)
#print(weight)
#print(distance )
#print(is_express)
#print( is_international)

if (weight <= 2.0 and distance <= 100) and (is_express == False and is_: 
    print('Free Shipping')
elif 