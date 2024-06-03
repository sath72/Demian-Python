'''
class Person:
    li=[]
    def __init__(self,sp):
        Person.li.append(sp)
    def disp(self):
        print(Person.li)

p1=Person('milk')
p1.disp()
p2=Person('Cola')
p2.disp()
p3=Person('Juice')
p3.disp()
'''

f=open("/Users/Demian/Desktop/pythonproject/abc.txt",'w')
for i in range(1,10):
    f.write('%d..\n'%i)
f.close()

f=open("/Users/Demian/Desktop/pythonproject/abc.txt",'r')
m=f.readlines()
f.close()

print(m)

for i in m:
    print(i,end='')



