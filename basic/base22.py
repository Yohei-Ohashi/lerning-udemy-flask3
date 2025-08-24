# try except

try:
    b = [10, 20, 30]
    # c = b.method_a()
    # a = b[4]
    # a = 10 / 0
except ZeroDivisionError as e:
    import traceback
    traceback.print_exc()
    #print(e, type(e))
    pass
except IndexError as e:
    print('indexerror発生')
    pass
except Exception as e:
    print('Exception: ', e, type(e))
else:
    # 例外が発生しなかった場合に実行される
    print('Else処理')
finally:
    # 例外が発生しても実行される
    print('Finally処理')

print('処理が完了しました。')