class Solution:
    def separateDigits(self, nums):
        num_str_list = map(str, nums)
        num_str = "".join(num_str_list)
        
        num_list = list(num_str)
        
        return list(map(int, num_list))
