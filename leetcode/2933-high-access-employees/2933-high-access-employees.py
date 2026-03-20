from collections import defaultdict
class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        access_times = sorted(access_times, key=lambda x:x[1])

        emp = defaultdict(list)

        for name,time in access_times:
            curr_time = int(time[:2])*60+int(time[2:])
            emp[name].append(curr_time)


        ans =[]
        for key,val in emp.items():
            left=0
            n= len(val)
            for right in range(2,n):
                if(val[right]-val[left] <60):
                    ans.append(key)
                    break
                else:
                    left+=1
                    right+=1
        return ans