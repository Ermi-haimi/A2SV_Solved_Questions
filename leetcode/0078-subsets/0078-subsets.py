class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def sub(arr1,arr2):
            nonlocal ans
            if(len(arr2) == 0):
                ans.append(arr1)
                return
            else:
                arr1_copy = arr1.copy()
                arr1.append(arr2[0])
                sub(arr1,arr2[1:])
                sub(arr1_copy,arr2[1:])
        sub([],nums)
        return ans