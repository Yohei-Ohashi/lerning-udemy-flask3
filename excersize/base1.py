# 1
num = 10

# 2
print(type(num))

# 3
num_str = str(num)

# 4
num_list = [num_str, '20', '30']
print(f'num_list = {num_list}')

# 5
num_list.append('40')

# 6
num_tuple = tuple(num_list)

# 7
input_str = input('数字を入力して下さい')
num_tuple += (input_str,)

# 8
num_set = {'40', '50', '60'}
print(f'num_tuple = {num_tuple}')
print(f'num_set = {num_set}')

# 9
print(set(num_tuple) | num_set)

# 10
num_dict = {num_tuple: num_str}

# 11
print(len(num_list))

# 12
print(num_dict.get('MyKey', 'Does not exist'))

# 13 リストに複数要素を追加
num_list.extend(['50', '60'])
print(f'num_list = {num_list}')

# 14
is_under_50 = int(input('数字を入力して下さい')) < 50
print(f'is_under_50 = {is_under_50}')

# 15
print(f'num_str = {num_str}')

# 16 メソッドを表示
print(dir(num_dict))