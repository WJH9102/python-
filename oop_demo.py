#!/usr/bin/env/ python3
# _*_ coding: utf-8 _*_


# 定义一个类，类名为Student
class Student(object):
    
    count = 0  # 类属性，所以对象共有

    def __init__(self, sno, sname):
        Student.count += 1
        self.sno = sno
        self.sname = sname

    def show(self):
        print(self.sno, self.sname)

    def __del__(self):
        print("{} killed me!".format(self.sno))


if __name__ == '__main__':
    student1 = Student(1001, "zs")
    student2 = Student(1002, "zs")
    student3 = Student(1003, "zs")
    student4 = Student(1004, "zs")
    student5 = Student(1005, "zs")
    student1.show()
    # del student1
    print(Student.count)
