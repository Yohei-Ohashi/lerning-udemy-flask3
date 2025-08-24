# 特殊メソッド

class Human:
    
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number
    
    # 
    def __str__(self):
        return self.name + ',' + str(self.age) + ',' + str(self.phone_number)
    
    # イコールの条件を変える
    def __eq__(self, other):
        return (self.name == other.name) and (self.phone_number == other.phone_number)

    # ハッシュ値を返す
    def __hash__(self):
        return hash(self.name + self.phone_number)

    # 真偽値を返す
    def __bool__(self):
        return  True if self.age >= 20 else False
    
    # 長さを返す
    def __len__(self):
        return len(self.name)

man = Human('Taro', 20, '08011111111')
man2 = Human('Taro', 18, '08011111111')
man3 = Human('Jiro2', 18, '09011111111')

man_str = str(man)
print(man_str)

print(man == man2)

set_man = {man, man2, man3}
for x in set_man:
    print(x)

if man:
    print('manはTrue')
if man2:
    print('man2はTrue')

print(len(man))
print(len(man2))
print(len(man3))