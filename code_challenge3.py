# Problem: Global Freight Calculator 

sender_name = input('Enter Your NAME: ')
type_of_item = input('Enter Your ITEM: ')
is_Fragile = input('Is the item FRAGILE? (True/False): ') == 'True'
weight = eval(input('How much does it WEIGHT? (kg): '))
distance = eval(input('How far is the DESTINATION? (km): '))
is_express = input('Do you want EXPRESS delivery? (True/False): ') == 'True'
is_international = input('Is this an INTERNATIONAL delivery? (True/False): ') == 'True'

base_cost = (weight * 2.50) + (distance * 0.15)

if weight <= 2 and distance <= 100 and is_express == False and is_international == False :
    print('Congratulations you got FREE SHIPPING!!')

elif is_international and is_express == True:
    total = (base_cost * 1.40) + 50
    print('International Express Fee:$',total)

elif is_express == True or (is_international == True and weight > 20):
    total = (base_cost * 1.20) + 25
    print('Express or Heavy International Fee:$ ',total)

elif weight > 30 or distance > 1000:
    total = base_cost + 30 
    print('Oversized Fee:$',total)

else:
    total = base_cost
    print('Standard Rate:$',total)
