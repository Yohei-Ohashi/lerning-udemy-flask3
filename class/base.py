# クラスの基本
class SchoolReport:
    school_name = 'サプー中学校'
    def __init__(self, student_name, scores):
        self.student_name = student_name
        self.scores = scores
    
    def calc_avg_score(self):
        total = sum(self.scores.values())
        avg = total / len(self.scores)
        return avg


sr_list = [
    SchoolReport('丈太郎 A', {'math': 100, 'jp': 30, 'en':50}),
    SchoolReport('鈴木 B', {'math': 20, 'jp': 59, 'en': 20}),
    SchoolReport('斎藤 C', {'math': 19, 'jp': 22, 'en': 19})
]

for sr in sr_list:
    print(sr.school_name)
    print(f'{sr.student_name}の3教科平均点: {sr.calc_avg_score()}')