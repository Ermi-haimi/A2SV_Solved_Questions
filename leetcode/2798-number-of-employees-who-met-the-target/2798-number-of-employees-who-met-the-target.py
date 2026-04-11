class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        hours.sort()
        for i,h in enumerate(hours):
            if(h>=target):
                return len(hours)-i
        return 0