# inner関数 ノンローカル変数

def outer():
    outer_value = '外側の変数'
    def inner():
        nonlocal outer_value
        outer_value = '内側の変数'
        print(f'inner: outer_value = {outer_value}, id = {id(outer_value)}')
    inner()
    print(f'outer: outer_value = {outer_value}, id = {id(outer_value)}')

outer()