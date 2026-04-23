class A:
    def methodA(self):
        print('this is class A')


class B(A):
    def methodB(self):
        print('this is class B')


class C(A):
    def methodC(self):
        print('this is class C')


class D(B, C):
    def methodD(self):
        print("this is class D")


inp = D()
inp.methodD()
inp.methodC()
inp.methodB()
inp.methodA()

#HybridInheritance = where more than one type of inheritance (like single, multiple, multilevel, hierarchical) are combined in a single program.