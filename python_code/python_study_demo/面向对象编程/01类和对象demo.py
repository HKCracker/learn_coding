class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 封装思想
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score > 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

std = Student('tom', 23)

grade = std.get_grade()
print(grade)