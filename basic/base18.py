# for

for i in range(10):
    print(i)

# ただ単に100回ループさせたい時_で表現する（お約束）
for _ in range(100):
    #print('A')
    pass

for i in range(2, 20, 3):
    print(i)

# sample = ['John', 'Paul', 'George', 'Ringo']
sample = ('John', 'Paul', 'George', 'Ringo')
for member in sample:
    print(member)

human = {
    'Name': 'Taro',
    'Age': 20,
    'Gender': 'Man'
}
for h in human:
    print(h, human[h])