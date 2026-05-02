"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importances = {} 
        subs = {}
        for empl in employees:
            importances[empl.id] = empl.importance
            subs[empl.id] = empl.subordinates

        print(subs)
        importance=0
        visited = set()

        def dfs(num):
            nonlocal importance
            if num not in visited:
                importance+=importances[num]
                for ids in subs[num]:
                    dfs(ids)
                  
        for emp in employees:
            if(emp.id == id):
                dfs(id)
        
        return importance


        