# ジェネレータ関数

def generator(max):
    print('ジェネレータ作成')
    for n in range(max):
        try:
            x = yield n
            print(f'x = {x}')
            print('yield実行')
        except ValueError as e:
            print('throwを実行しました')

gen = generator(10)
next(gen)
gen.send(100)
# gen.throw(ValueError('Invalid Value'))
# gen.close()
next(gen)
# for x in gen:
#     print(f'x = {x}')

# send
