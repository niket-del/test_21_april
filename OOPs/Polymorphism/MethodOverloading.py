class addition:
    def add(self, a=0, b=0, c=0):
        print(a + b + c)


sum1 = addition()
sum1.add(2, 3)
sum1.add(2, 3, 9)
sum1.add(3)

#same method name have diffrent perameters like python doesnot support actual overLoading
#main overloading mean is like multiple method in same class have same name but diffrent perameters are the correct one chooses by compiler automatically


# class Math:
#     def add(a, b):
#         print(a + b)
#
#     def add(a, b, c):
#         print(a + b + c)
#
#
# inp = Math()
# inp.add(4, 5)

#now the above code is actual overloading but it is not working in python