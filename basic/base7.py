# 文字列型

fruit = 'apple'
print(fruit)
print(type(fruit))

print(fruit * 10)
fruit_10 = fruit * 10
print(fruit_10)

new_fruit = fruit + ' banana'
print(new_fruit)

fruits = """apple
banana
grape
"""
print(fruits)

fruit = 'banana'
print(fruit[-1])

# encode, decode => bytes[]
byte_fruit = fruit.encode('utf-8')
print(byte_fruit)
print(type(byte_fruit))

str_fruit = byte_fruit.decode('utf-8')
print(str_fruit)
print(type(str_fruit))

# count

msg = 'ABCDEABC'
print(msg.count('ABCDEF'))

# startswith, endswith
# 何で始まるか、何で終わるか

print(msg.startswith('ABECD'))
print(msg.endswith('DC'))

# strip, rstrip, lstrip
# 文字列の両端、右端、左端の空白を削除

msg = ' ABC '
print(msg)
print(msg.strip())
msg = 'ABCDEFABC'
print(msg.strip('CBA'))
print(msg.lstrip('CBA'))
print(msg.rstrip('CBA'))

# upper, lower, swapcase, replace, capitalize
# replaceが最もよく使われる

msg = 'abcABC'
msg_u = msg.upper()
msg_l = msg.lower()
msg_s = msg.swapcase()
print(msg_u, msg_l, msg_s)

msg = 'ABCDEABC'
msg_r = msg.replace('ABC', 'FFF', -1)
print(msg_r)

msg = 'hello WoRld'
print(msg.capitalize())

# 文字列の一部取り出し、 format, isloewr, isupper

msg = 'hello, my name is taro'
print(msg[1:10:3])
print('hello {}'.format('Taro'))
# Python3.6以降はf-stringが使える
name = 'Jiro'
print(f'hello {name}')
print(f'{name=}') # Python3.8以降

# islower, isupper
#　小文字か、大文字か

msg = 'APPLE'
print(msg.islower())
print(msg.isupper())

# find, index, rfind, rindex
# 文字列の中に指定した文字列があるか、ある場合はその位置を返す

msg = 'ABCDEABC'
# findは見つからない場合は-1を返す
print(msg.find('ABC'))
print(msg.rfind('ABC'))
print(msg.find('ABCE'))
# indexは見つからない場合はエラーになる
print(msg.index('ABC'))
print(msg.rindex('ABC'))
# print(msg.index('ABCE'))

