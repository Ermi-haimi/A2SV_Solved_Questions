class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        nho = len(houses)
        nht = len(heaters)
        def pos(rad):
            hidx = 0
            tidx = 0

            while hidx < nho:
                if tidx >= nht:
                    return False

                mn = heaters[tidx] - rad
                mx = heaters[tidx] + rad
                if(houses[hidx] < mn):
                    return False
                if(houses[hidx] > mx):
                    tidx+=1
                else:
                    hidx+=1
            return True
        
        l = 0
        r = 10**9
        ans = r
        while(l<=r):
            mid = l+(r-l)//2
            if pos(mid):
                ans = mid
                r=mid-1
            else:
                l = mid+1
        return ans
            

            