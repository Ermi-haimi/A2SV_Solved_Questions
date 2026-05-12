class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        st = []
        mn = float('inf')
        for num in nums:
            while(st and st[-1][0] <= num):
                st.pop()
            if(st and st[-1][1] < num):
                print(st,num)
                return True
            mn = min(mn,num)
            st.append((num,mn))
            
        return False


