# Dictionary(辞書型)

car = {
    'brand': 'Toyota',
    'model': 'Prius',
    'year': 2015,
    1: 100
}
print(car['brand'])
print(car.get('bran', 'Does not exist'))

print(car[1])

print(car.keys()) # キー一覧
print(car.values()) # 値一覧
print(car.items()) # キーと値のペア一覧

for k, v in car.items():
    print(f'key = {k}, value = {v}')

if 'brand' in car:
    print(f'carのブランドは{car["brand"]}')
