class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        arr = [0,0,0]
        for num in nums:
            arr[num]+=1
        
        i=0
        for ind,num in enumerate(arr):
            for _ in range(num):
                nums[i]=ind
                i+=1
        


        