# インスタンスメソッド、クラスメソッド、スタティックメソッド

class Human:
    
    class_name = "Human"  # クラス変数
    
    def __init__(self, name, age):  # コンストラクタ
        self.name = name
        self.age = age
    
    def print_name_age(self):  # インスタンスメソッド
        print('インスタンスメソッド実行')
        print(f'name = {self.name}, age = {self.age}')
    
    @classmethod
    def print_class_name(cls, msg):  # クラスメソッド
        print('クラスメソッド実行')
        print(cls.class_name)  # クラス変数
        print(msg)
        # インスタンス変数にはアクセスできない
        # print(self.name)  # クラスメソッドではselfは使えない
        # print(cls.name)  # Humanクラスにはnameというクラス変数がない
    
    @staticmethod
    def print_msg(msg):  # スタティックメソッド
        print('スタティックメソッド実行')
        print(msg)

# インスタンスメソッドを呼び出す
Human.print_class_name('こんにちは')

# インスタンスメソッドを実行
man = Human('桜木', 18)
man.print_name_age()

# スタティックメソッドを実行
man.print_msg('Hello, static')
Human.print_msg('Hello, static')