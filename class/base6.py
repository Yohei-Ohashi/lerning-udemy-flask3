# クラスの継承

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print(f"hello {self.name}")
    
    def say_age(self):
        print(f'{self.age} years old')

class Employee(Person):  # Personの機能を継承
    def __init__(self, name, age, number):
        super().__init__(name, age)  # super()とすることで、親クラスの__init__を呼び出し、nameとageを初期化
        self.number = number
    
    def say_number(self):
        print(f'my number is = {self.number}')
    
    def greeting(self):  # オーバーライド
        super().greeting()  # 親クラスのgreetingを呼び出し
        print(f'I\'m employee phone_number = {self.number}')
    
    # def greeting(self, age):  # 上のgreetingを上書きしてしまうのでPythonではオーバーロードはできない
    #     print('オーバーロード')
man = Employee('Tonegawa', 45, '08011111111')
man.greeting()
man.say_age()
man.say_number()