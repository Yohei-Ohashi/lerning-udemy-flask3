# enumerate, zip, while

fruits = ['grape', 'Pine', 'Apple']

for index, fruit in enumerate(fruits):
    print(f'index: {index}')
    print(f'fruit: {fruit}')

# zip
classA = ['Taro', 'Hanako', 'Jiro']
classB = ['Katsuo', 'Wakame', 'Tara']

for A, B in zip(classA, classB):
    print(f'classA student: {A}')
    print(f'classB student: {B}')

# while
count = 0
while count < 10:
    print(count)
    count += 1