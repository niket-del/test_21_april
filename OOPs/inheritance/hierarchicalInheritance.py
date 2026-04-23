class father:
    def fatherMethod(self):
        print('this is a father class')


class child1(father):
    def child1Method(self):
        print('this is a child1 class')


class child2(father):
    def child2method(self):
        print('this is the child2 class')


ch1 = child1()
ch2 = child2()
ch1.fatherMethod()
ch2.fatherMethod()


#Hierarchical Inheritance : so in hierarchical inheritance multiple class inherit the property of  same clss
#for above example there is 2 child class inherit the property of single parent class.
