class mathdojo (object):
    def __init__(self,x):
        self = self
        self.num3 = 0
        
    def add(self,num, *nums):
        self.num = num
        x=self.num
        self.nums = nums

        for i in range(0,len(self.nums)):
            x += self.nums[i]
        self.num3 += x
        return self

    def subtract(self,num, *nums):
        self.num = num
        x=self.num
        self.nums = nums
        for i in range(0,len(self.nums)):
            x += self.nums[i]
        self.num3 -= x
        return self


    def result(self):
        print "The answer is ",self.num3

md = mathdojo(0)

md.add(2).add(2,5).subtract(3,2).result()
md.add(1, 3,4).add(3,5,7,8, 2,4.3,1.25).subtract(2, 2,3, 1.1,2.3).result()