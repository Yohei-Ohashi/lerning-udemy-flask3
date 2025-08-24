# セット

set_a = {'a', 'b', 'c', 'd', 'a', 12}
print(set_a)
print('e' in set_a)
print('a' in set_a)
print('a' not in set_a)

print(len(set_a))

# add, remove, discard, pop, clear
# 要素を追加
set_a.add('A')
print(set_a)
# 要素を削除
set_a.remove('a')
print(set_a)
# 要素を削除
set_a.discard(12)
print(set_a)
# 要素を削除
value = set_a.pop()
print(value, set_a)
# 全ての要素を削除
set_a.clear()
print(set_a)