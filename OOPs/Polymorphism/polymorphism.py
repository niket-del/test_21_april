class Birds:
    def fly(self, name=None):
        if name == 'parrot':
            print(name, 'can fly....!')
        elif name == 'penguin':
            print(name, 'cannot fly...!')
        elif name is None:
            print('Input is unavailable....!')
        else:
            print('unknown Bird ....!')


bird = Birds()
bird.fly("parrot")
bird.fly('penguin')
bird.fly()
bird.fly('hen')

#where a single method name can have multiple behaviors depending on the object calling it.
