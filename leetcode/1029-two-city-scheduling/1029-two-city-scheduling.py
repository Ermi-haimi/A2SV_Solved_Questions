class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        diff = {}
        for i in range(n):
            diff[i]=abs(costs[i][0]-costs[i][1])
        
        diff = dict(sorted(diff.items(), reverse=True, key=lambda x:x[1]))
        choosen = [False]*n
        cost=0
        a=0
        b=0
        for key in diff:
            if(costs[key][0]>costs[key][1]):
                cost+=costs[key][1]
                b+=1
            else:
                cost+=costs[key][0]
                a+=1
            choosen[key] = True
            if b == n/2 or a == n/2:
                break

        if(a==n/2):
            for i in range(n):
                if(not choosen[i]):
                    cost+=costs[i][1]
        else:
            for i in range(n):
                if(not choosen[i]):
                    cost+=costs[i][0]

        return cost


        
                

        