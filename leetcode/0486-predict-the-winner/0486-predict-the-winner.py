class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def takes(left,right):
            if(left > right):
                return 0
            
            take_left = nums[left]-takes(left+1,right)
            take_right = nums[right]-takes(left,right-1)

            return max(take_left, take_right)
        
        return takes(0,len(nums)-1) >=0
