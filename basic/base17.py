# all, any関数

# 全てTrueかどうか
if all((True, True, True)):
    print('全てTrueです')
if all((True, 10 < 20, 'a' == 'a')):
    print('全てTrueです')
# FalseがあるとFalse判定で実行されない
if all((30 < 10, 10 < 20, 'a' == 'a')):
    print('全てTrueです')

# いずれかがTrueかどうか
if any((False, True, True)):
    print('いずれかがTrueです')
if any((30 < 10, 10 < 20, 'a' == 'a')):
    print('いずれかがTrueです')
# 全てFalseかどうか
if not any((30 < 10, 10 < 5, 'a' == 'b')):
    print('全てFalseです')