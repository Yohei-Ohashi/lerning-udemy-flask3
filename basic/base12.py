# タプル

fruits = ('apple', 'banana', 'lemon')

print(fruits)
print(type(fruits))
print(fruits[0])
# fruits[1] = 'grape'
fruits = fruits + ('grape',)
print(fruits)

list_fruits = ['apple', 'banana']
fruits = tuple(list_fruits)
print(fruits)
print(fruits.count('apple'))
print(fruits.index('banana'))

pos = (135, 35)

countries = {pos: 'Japan'}

print(countries.get((135, 35)))