# リスト内包表記

# タプルを作成
list_a = (1, 2, 3, 'a', 4, 'b')

# list_aのリストを作成
list_b = [x * 2 for x in list_a if type(x) == int]
print(list_a)
print(list_b)

list_c = [x for x in range(100) if x % 7 == 0]
print(list_c)

dict_a = {
    'a': 'Apple',
    'b': 'Banana'
}
list_c = [dict_a[x] for x in list_a if type(x) == str]
print(list_c)

# 内包表記でジェネレータを作成する
generator_a = (x for x in range(100))
print(type(generator_a))

# 内包表記でセットを作成する
set_a = {x for x in range(100)}
print(type(set_a))

# 内包表記でタプルを作成する
tuple_a = tuple(x for x in range(100))
print(type(tuple_a))


def func(n):
    for x in range(2, n):
        if n % x == 0:
            return True
    return False

list_a = [x for x in range(100) if func(x) == False]
print(list_a)