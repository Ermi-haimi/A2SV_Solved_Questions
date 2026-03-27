class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def comb(curr,choosen):
            if(len(choosen) == k):
                ans.append(choosen[:])
                return
            
            for num in range(curr,n+1):
                choosen.append(num)
                comb(num+1,choosen)
                choosen.pop()
        
        ans = []
        comb(1,[])
        return ans