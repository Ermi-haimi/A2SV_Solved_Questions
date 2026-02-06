from collections import defaultdict
class Solution:
    def findDuplicate(self, paths):
        same_content=defaultdict(list)
        for path in paths:
            path_list = path.split(" ")
            for i in range(1,len(path_list)):
                ind = path_list[i].find(".")
                add = path_list[0] +"/"+path_list[i][:ind+4]
                same_content[path_list[i][ind+5:-1]].append(add)
        
        ans = []
        for key,items in same_content.items():
            if len(items)>1:
                ans.append(items)
        return ans
            