#测试多重继承

class A:
    def aa(self):
        print("aa1")

    def say(self):
        print("say holle")

class B:
    def bb(self):
        print("bb2")

    def say(self):
        print("say world")

class C(B,A):
    def cc(self):
        print("cc3")

c=C()
c.cc()
c.bb()
c.aa()
print(C.mro())
c.say()