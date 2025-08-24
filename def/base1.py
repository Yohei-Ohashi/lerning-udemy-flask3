# 関数

def print_hello():
    print('Hello, World')

print_hello()

def num_max(a: int, b: int) -> int:
    print(f'a = {a}, b = {b}')
    if a > b:
        return a
    else:
        return b

print(num_max(b=100, a=20))
print(num_max(10, 20))