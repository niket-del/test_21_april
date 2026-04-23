def lenOfString(str1):
    count = 0
    for i in range(len(str1)):
        count += 1

    return count


str1 = 'niket'
print(lenOfString(str1))

#Approach : go through the each character of string and every time increase the count untill thw loop stop
#solution : initiate count with 0, now ittrate the loop till the  len of string and and increase the count

class lenOfString:
    def findLen(self,str1,count=0):
        self.str1 = str1
        self.count = count
        self.count = 0
        for i in range(len(str1)):
            self.count += 1
        return self.count

input1 = lenOfString()
str1 = 'efkjncbehfbveikhbvefv'
print(input1.findLen(str1))

#solution: same as the above just use the class and object  here I create a class name is lenOfString
# and in last just create object as input1 and call the class and using that object call the function findLen
