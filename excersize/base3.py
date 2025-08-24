# じゃんけん 勝った場合はループの外、負けた場合は3回でループの外、あいこはあいこと表示
# 相手は必ずグー、チョキ、パーの順番で手を出す。

def generate_enemy_hand():
    while True:
        yield 1
        yield 2
        yield 3

def is_win(player, enemy):
    if player == 1 and enemy == 2:
        return True
    elif player == 2 and enemy == 3:
        return True
    elif player == 3 and enemy == 1:
        return True
    else:
        return False

janken_hand = {
    1: 'グー',
    2: 'チョキ',
    3: 'パー'
}

lose_count = 0
enemy_hands = generate_enemy_hand()

while True:
    player_hand = int(input('何を出しますか？ 1:グー, 2:チョキ, 3:パー'))
    if player_hand not in [1, 2, 3]:
        print('1~3の数字を入力して下さい')
        continue
    enemy_hand = next(enemy_hands)
    print(f'あなたの出した手: {janken_hand[player_hand]}、相手の出した手: {janken_hand[enemy_hand]}')
    if player_hand == enemy_hand:
        print('あいこ')
        continue
    if is_win(player_hand, enemy_hand):
        print('あなたの勝ちです')
        break
    else:
        lose_count += 1
        if lose_count == 3:
            print('あなたの負けです')
            break
        else:
            print('あなたの負けです。再チャレンジ')