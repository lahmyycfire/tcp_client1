import json

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student('zhangsan', 18)
print(s1)
print(s1.__dict__)
# 将class序列化成json
j1 = json.dumps(s1, default=lambda obj: obj.__dict__)
print(j1)

# 将json反序列化成class
def dict2student(j):
    return Student(j['name'], j['age'])

s2 = json.loads(j1, object_hook=dict2student)
print(s2)
