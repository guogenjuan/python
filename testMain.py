#!/usr/bin/python3
#_*_coding:UTF-8 _*_

class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()
