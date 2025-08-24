# 1~100 3:Fizz, 5:Buzz, 15:FizzBuzz

num = 0
while (num := num + 1) < 101:
    if num % 3 == 0 and num % 5 ==0:
        print(f'{num}: FizzBuzz')
    elif num % 3 == 0:
        print(f'{num}: Fizz')
    elif num % 5 == 0:
        print(f'{num}: Buzz')
    else:
        print(f'{num}: ')