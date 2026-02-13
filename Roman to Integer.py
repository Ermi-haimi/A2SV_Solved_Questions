class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        point = 0
        n = len(s)
        while(point<n):
            count = 0
            if(s[point] =="M"):
                while(point<n and s[point] =="M"):
                    count+=1
                    point+=1
                num+=count*1000
                point-=1
            elif(s[point] == "D"):
                num+=500
            elif(s[point] == "C"):
                if(point<n-1 and s[point+1] == "D"):
                    num+=400
                    point+=1
                elif(point<n-1 and s[point+1] == "M"):
                    num+=900
                    point+=1
                else:
                    while(point<n and s[point] =="C"):
                        count+=1
                        point+=1
                    num+=count*100
                    point-=1
            elif(s[point] == "L"):
                num+=50
            elif(s[point] == "X"):
                if(point<n-1 and s[point+1] == "L"):
                    num+=40
                    point+=1
                elif(point<n-1 and s[point+1] == "C"):
                    num+=90
                    point+=1
                else:
                    while(point<n and s[point] =="X"):
                        count+=1
                        point+=1
                    num+=count*10
                    point-=1
            elif(s[point] == "V"):
                num+=5
            else:
                if(point<n-1 and s[point+1] == "V"):
                    num+=4
                    point+=1
                elif(point<n-1 and s[point+1] == "X"):
                    num+=9
                    point+=1
                else:
                    while(point<n and s[point] =="I"):
                        count+=1
                        point+=1
                    num+=count*1
                    point-=1
            point+=1
        
        return num
            
