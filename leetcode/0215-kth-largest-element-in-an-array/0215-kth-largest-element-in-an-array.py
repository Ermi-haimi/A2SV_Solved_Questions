class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_h = []
        for num in nums:
            if(len(min_h) <k):
                heappush(min_h, num)
            else:
                curr_min = heappop(min_h)
                if(curr_min < num):
                    heappush(min_h,num)
                else:
                    heappush(min_h,curr_min)
        return min_h[0]


        