# if and or not

# msg = input('信号の色は？')
# if msg == 'blue':
#     print('進め')
# elif msg == 'red':
#     print('止まれ')
# else:
#     print('それ以外の処理')

# age = int(input('年齢を入力して下さい'))
# if age < 20:
#     print('20未満')
# elif age <= 40:
#     print('20以上、40以下です')
# elif age >= 60:
#     print('60以上です')
# else:
#     print('それ以外の年齢')
    
# and or not

gender = input('性別を入力して下さい')
age = int(input('年齢を入力して下さい'))

if gender == 'man' or age < 20:
    print('男性もしくは20未満です')

if not gender == 'man':
    print('男性ではありません')
    