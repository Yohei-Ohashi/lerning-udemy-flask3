# 演習4

class CharacterAlreadyExistException(Exception):
    ''' 同じキャラクターを登録した場合に作成する例外
    '''
    pass

class AllCharacters:
    ''' キャラクターの状態を管理するクラス
        
        同じキャラクターを登録した場合は、characterAlreadyExistExceptionを作成して返す
    '''
    all_characters = []
    alive_characters = []
    dead_characters = []
    
    @classmethod
    def character_append(cls, name):
        if name in cls.all_characters:
            raise CharacterAlreadyExistException('キャラクターはすでに存在します')
        cls.all_characters.append(name)
        cls.alive_characters.append(name)
        
    @classmethod
    def character_delete(cls, name):
        cls.dead_characters.append(name)
        cls.alive_characters.remove(name)

class Character:
    ''' キャラクターのクラス
    '''
    
    def __init__(self, name, hp, offence, defence):
        AllCharacters.character_append(name)
        self.name = name
        self.hp = hp
        self.offence = offence
        self.defence = defence
    
    def attack(self, enemy, critical_point=1):
        ''' 敵インスタンスのHPが自分のoffence - 敵のdefenceの値だけ減る
            (自分のoffence - 敵のdeffenceがマイナスの場合は1になる)
        '''
        if self.hp <= 0:
            print(f'{self.name}は死んでいます')
            return
        attack_point = self.offence - enemy.defence
        attack_point = 1 if attack_point < 0 else attack_point
        enemy.hp -= attack_point * critical_point
        
        if enemy.hp <= 0:
            AllCharacters.character_delete(enemy.name)
    
    def critical_hit(self, enemy):
        ''' attackメソッドの倍のダメージを与える '''
        self.attack(enemy, 2)



character_a = Character('Player', 10, 5, 3)
character_b = Character('Enemy', 8, 6, 2)

print(character_b.hp)
character_a.critical_hit(character_b)
print(character_b.hp)
print(AllCharacters.alive_characters)
character_a.attack(character_b)
print(AllCharacters.alive_characters)
print(AllCharacters.dead_characters)
character_b.attack(character_a)

character_c = Character('Player', 10, 5, 3)
