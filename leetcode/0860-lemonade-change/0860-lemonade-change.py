class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n = len(bills)
        count5 = 0
        count10=0
        for i in range(n):
            if(bills[i] == 5 ):
                count5+=1
            elif(bills[i] == 10):
                if(count5==0):
                    return False
                count10+=1
                count5-=1
            else:
                left = 15
                if count10 >0:
                    count10-=1
                    left=5
                if(left ==5):
                    if(count5>0):
                        count5-=1
                    else:
                        return False
                else:
                    if(count5>2):
                        count5-=3
                    else:
                        return False
        
        return True

        

        