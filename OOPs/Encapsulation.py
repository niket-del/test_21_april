class bank:
    def __init__(self, acc, name, balance):
        self.acc = acc
        self.name = name
        self.__balance = balance

    def credit(self, amount):
        self.__balance += amount
        print('Hi', self.name, 'Credit transaction in your account', self.acc % 10000, 'is done your updated balace is',
              self.__balance)

    def debit(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print("Hi", self.name, 'Debit transaction of', amount, 'is done for account', self.acc % 10000,
                  'current balance is', self.__balance)
        else:
            ("Hi", self.name, 'Debit transaction is Failed', self.acc, 'current balance is', self.__balance,'you dont have sufficient balance')

    def chkBalance(self):
        print('Hi', self.name, 'your current balance for', self.acc % 10000, 'is', self.__balance)


accoun1 = bank(551702120002228, 'Niket', 45000)
accoun1.credit(45000)
accoun1.debit(10000)
accoun1.chkBalance()


#bundle data (variables) and methods (functions) together into a single unit (class) is knows as encapsulation.
#in example multiple methods like credit , debit and check balance manage by class bank