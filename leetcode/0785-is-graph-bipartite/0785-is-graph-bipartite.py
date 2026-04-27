class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0]*n
        visited = set()

        def dfs(parent,num):
            for node in graph[num]:
                if(node not in visited):
                    colors[node]=parent
                    visited.add(node)
                    if not dfs(-parent,node):
                        return False
                else:
                    if(colors[node] != parent):
                        return False
            return True

        for i in range(n):
            if(i not in visited):
                colors[i] = 1
                ret = dfs(-1,i)
                if(not ret):
                    return False
        return True
        