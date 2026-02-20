class Solution:
    def maxCoins(self, piles) -> int:
        piles.sort()
        n= len(piles)
        end = int(n/3)-1
        ans = 0
        print(piles)
        for i in range(n-2,end,-2):
            ans+=piles[i]
        return ans
        