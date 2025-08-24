# if 1行 lambda

y = 10
# yが0より大きい場合は0、そうでない場合は1を代入する
x = 0 if (y - 20) > 0 else 1
# print(x)

lambda_a = lambda x: x * x
print(lambda_a(10))

# 引数を複数設定でき、デフォルト値も設定できる
lambda_b = lambda x, y, z=5: x * y * z
print(lambda_b(2, 3))
print(lambda_b(2, 3, 4))

# 条件式を用いたlambda
lambda_c = lambda x, y: y if x < y else x
print(lambda_c(6, 4))