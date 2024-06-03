
'''
class Person:
    def __init__(self, name, age, sex, mbti):
        self.name=name
        self.age=age
        self.sex=sex
        self.MBTI=mbti
    def disp(self):
        print(self.name, self.age, self.sex, self.MBTI)

p1=Person('Demian', 51, 'Male', 'INFJ')
p2=Person('Catherine', 49, 'Female', "INFP")

p1.disp()
p2.disp()
'''

'''
class Person:
    def __init__(self):
        self.name=input('Name: ')
        self.age=int(input('Age: '))
    def disp(self):
        print(self.name+':'+str(self.age))

li=[]
for i in range(3):
    li.append(Person())
    li[i].disp()
for i in li:
    i.disp()
    
print(li[0].name)
'''
'''
class Sj:
    def __init__(self):
        self.__eng=77

    def geteng(self):
        return self.__eng
    def seteng(self,eng):
        self.__eng=eng

s1=Sj()
print(s1.geteng())
s1.seteng(100)
print(s1.geteng())
'''
'''
class Person:
    def __init__(self):
        self.name='Demian'
        self.age=25
    def say(self):
        pass
    def disp(self):
        print(self.name+':'+str(self.age))

class Korean(Person):
    def __init__(self):
        super().__init__()
        self.lang='Korean'
    def say(self):
        print('안녕하세요')
class American(Person):
    def __init__(self):
        super().__init__()
        self.lang='English'
    def say(self):
        print('Hello')

p1=Person()
print(p1.name, p1.age)

k1=Korean()
print(k1.name, k1.age, k1.lang)
k1.say()

a1=American()
print(a1.name, a1.age, a1.lang)
a1.say()
'''

class Point:
    def __init__(self):
        self.x=int(input('x= '))
        self.y=int(input('y= '))
    def disp(self):
        pass

class Rect(Point):
    def __init__(self):
        super().__init__()
        self.w = int(input('w= '))
        self.h = int(input('h= '))
    def disp(self):
        print('Rectangle', self.x, self.y, self.w, self.y)

class Circle(Point):
    def __init__(self):
        super().__init__()
        self.r = int(input('r= '))

    def disp(self):
        print('Circle', self.x, self.y, self.r)

def main():
    li=list()
    while True:
        s=input('1. Square, 2. Circle, 3. Retrieve, 4. Finish : ')
        if s=='1':
            li.append(Rect())
        if s=='2':
            li.append(Circle())
        if s=='3':
            for i in li:
                i.disp()
        if s=='4':
            break
print('Program Stop')

main()

