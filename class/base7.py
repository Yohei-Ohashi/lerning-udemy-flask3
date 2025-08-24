# クラスの多重継承

class ClassA:
    
    def __init__(self, name):
        self.name = name
    
    def print_a(self):
        print('ClassAのメソッド実行')
        print(f'a = {self.name}')
    
    def print_hi(self):
        print('A hi')

class ClassB:
    
    def __init__(self, name):
        self.name = name
    
    def print_b(self):
        print('ClassBのメソッド実行')
        print(f'b = {self.name}')
    
    def print_hi(self):
        print('B hi')

class NewClass(ClassA, ClassB):
    
    def __init__(self, a_name, b_name, name):
        ClassA.__init__(self, a_name)
        ClassB.__init__(self, b_name)
        self.name = name
    
    def print_new_name(self):
        print(f'name = {self.name}')
    
    def print_hi(self):
        ClassA.print_hi(self)
        ClassB.print_hi(self)
        print('NewClass hi')


sample = NewClass('AName', 'BName', 'New Class Name')

sample.print_a()
sample.print_b()
sample.print_new_name()
sample.print_hi()


# RPG風な構成で表現した場合のコード
class WizardClass:
    
    def __init__(self, name):
        self.name = name
        self.magic_power = 100
    
    def cast_spell(self):
        print('WizardClassの魔法を実行')
        print(f'魔法使い {self.name} が呪文を唱えた！')
    
    def print_hi(self):
        print('Wizard hi')

class SwordFighterClass:
    
    def __init__(self, name):
        self.name = name
        self.sword_power = 80
    
    def swing_sword(self):
        print('SwordFighterClassの剣技を実行')
        print(f'剣士 {self.name} が剣を振った！')
    
    def print_hi(self):
        print('Sword hi')

class MagicSwordFighterClass(WizardClass, SwordFighterClass):
    
    def __init__(self, wizard_name, sword_name, name):
        # 親クラスの初期化を明示的に呼び出し
        WizardClass.__init__(self, wizard_name)
        SwordFighterClass.__init__(self, sword_name)
        self.name = name
        self.combined_power = 150
    
    def magic_sword_attack(self):
        print(f'魔剣士 {self.name} の必殺技！')
        print('魔法と剣技を組み合わせた攻撃！')
    
    def print_hi(self):
        WizardClass.print_hi(self)
        SwordFighterClass.print_hi(self)
        print('MagicSword hi')

# インスタンスを作成してテスト
msfc = MagicSwordFighterClass('ガンダルフ', 'アラゴルン', '魔剣士レジェンド')

print("=== 魔剣士の能力テスト ===")
msfc.cast_spell()      # WizardClassのメソッド
msfc.swing_sword()     # SwordFighterClassのメソッド
msfc.magic_sword_attack()  # MagicSwordFighterClass独自のメソッド
msfc.print_hi()        # オーバーライドされたメソッド

print(f"\n=== 属性の確認 ===")
print(f"魔法使い名: {msfc.name} (WizardClass)")
print(f"剣士名: {msfc.name} (SwordFighterClass)")
print(f"魔剣士名: {msfc.name} (MagicSwordFighterClass)")
print(f"魔法力: {msfc.magic_power}")
print(f"剣技力: {msfc.sword_power}")
print(f"総合力: {msfc.combined_power}")