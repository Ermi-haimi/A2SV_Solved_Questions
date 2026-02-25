class Solution:
    def dividePlayers(self, skill) -> int:
        skill.sort()
        left = 0
        right = len(skill)-1
        ans = 0
        sk = skill[left]+skill[right]
        while(left<right):
            
            if(skill[left]+skill[right] != sk):
                return -1
            curr = skill[left]*skill[right]
            ans+=curr
            left+=1
            right-=1
        
        return ans