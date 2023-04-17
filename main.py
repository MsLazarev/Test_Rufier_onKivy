class bbb():
    def __init__(self):
        pass
    def proverka(self):
        global a
        a += 1
        print(a, "bbb")

class aaa():
    def __init__(self):
        pass
    def proverka1(self):
        global a
        a = 3
        print(a, "aaa")
a = 1
b = aaa()
c = bbb()
b.proverka1()
c.proverka()