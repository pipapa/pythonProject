class Student:
    company = "建苏之家"   # 类属性
    count = 0            # 类属性
    score_sum=0
    fmaily_members=[]
    def __init__(self, name, score):
        self.name = name     # 实例属性
        self.score = score   # 实例属性
        Student.count += 1
        Student.score_sum+=self.score
        Student.fmaily_members.append(self.name)

    def say_score(self):  # 实例方法
        print("我家是：", Student.company)
        print("{}的得分是:{}".format(self.name,self.score))


s1=Student("陈建苏",76)
s2=Student("陈子轩",100)
s3=Student("柏宏兰",58)
s1.say_score()
Student.say_score(s2)
Student.say_score(s3)
print("家庭成员数量：",Student.count)
print("建苏之家的平均分数是：{}".format(Student.score_sum/Student.count))
print("家庭成员",Student.fmaily_members)
