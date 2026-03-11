class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        n = len(nums1)
        ans = [-1]*n
        indice = {}
        for ind, num in enumerate(nums1):
            indice[num] =ind 
        for ind,num in enumerate(nums2):
            while(st and st[-1] < num):
                curr = st.pop()
                if curr in indice:
                    ans[indice[curr]] = num

            st.append(num)
        for num in st:
            if(num in indice):
                ans[indice[num]]=-1     
        
        return ans


        