class father:
    def fatherMethod(self):
        print('this is a father class')


class mother:
    def motherMethod(self):
        print('this is a mother class')


class child(father, mother):
    def childmethod(self):
        print('this is the child class')


ch = child()
ch.fatherMethod()
ch.motherMethod()
ch.childmethod()