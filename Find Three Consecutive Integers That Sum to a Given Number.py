class Solution:
    def sumOfThree(self, num: int):
        ans = []
        if(num%3 ==0):
            third = int(num//3)
            ans = [third-1,third,third+1]
        return ans