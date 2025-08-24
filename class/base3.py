# コンストラクタ(__init__)、デストラクタ(__del__)

class SampleClass:
    def __init__(self, msg, name=None): # コンストラクタ
        print('コンストラクタが呼ばれました')
        self.msg = msg # インスタンス変数
        self.name = name # インスタンス変数
    
    def __del__(self): # デストラクタ
        print('デストラクタが実行されました')
        print(f'name = {self.name}')

    def print_msg(self):
        print(self.msg)
    
    def print_name(self):
        print(self.name)

var_1 = SampleClass('Hello', 'Jiro')
var_1.print_msg()
var_1.print_name()

del var_1