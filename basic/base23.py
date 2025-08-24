# raise 例外自作

class MyException(Exception):
    pass

def devide(a, b):
    if b == 0:
        raise ZeroDivisionError('0では割り切れません')
    else:
        return a/ b

def devide2(a, b):
    return a / b

try:
    c = devide(10, 0)
except Exception as e:
    print('devide')
    print(e, type(e))

try:
    c = devide2(10, 0)
except Exception as e:
    print('devide2')
    print(e, type(e))

try:
    raise MyException('自作例外')
except MyException as e:
    print('MyException')
    print(e, type(e))

print('処理が完了しました。')