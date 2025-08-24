# サブジェネレータ

def sub_sub_generator():
    yield 'Sub Subのyield'
    return 'sub subのreturn'

def sub_generator():
    yield 'subのyield'
    res = yield from sub_sub_generator()
    print(f'sub res = {res}')
    return 'subのreturn'

def generator():
    yield 'generatorのyield'
    res = yield from sub_generator()
    print(f'gen res = {res}')
    return 'generatorのreturn'

gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))