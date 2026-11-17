fruit_basket = []

fruit_basket = ['saging', 'ubas', 'santol', 'apple', 'sharmaine', 'sinigwelas', 'sampalok', 'mango']
print(fruit_basket)

# list 
fruit_basket.append('avocado')
fruit_basket.append('dragon fruit')
fruit_basket.append('watermelon')
fruit_basket.append('papaya')
fruit_basket.append('strawberry')
print(fruit_basket)
fruit_basket.insert(1, 'pineapple')
print(fruit_basket)

# removal or deletion of items within a list
fruit_basket.pop()
fruit_basket.pop()
fruit_basket.pop()
print(fruit_basket)
fruit_basket.remove('sampalok')
print(fruit_basket)

#list slicing
print(fruit_basket[6])
print(fruit_basket[0])
print(fruit_basket[-1])
print(fruit_basket[0 : 5])