class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if(n ==1):
            return True
        if(nums[0] ==0):
            return False

        possible = True
        i = n-2
        while(i >0):
            if nums[i] == 0:
                possible=False
                step = 1
                i-=1
                while(i>=0 and nums[i] <= step):
                    step+=1
                    i-=1
                if(i>=0):
                    possible = True
                else:
                    break
            else:
                i-=1
        if(possible):
            return True
        return False


