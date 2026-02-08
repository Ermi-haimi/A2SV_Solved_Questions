class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        while(num>0):
            if num>=1000:
                ad = num//1000
                num = num%1000
                ans+=ad*"M"
            elif(num>=500):
                if(num >=900):
                    ans +="CM"
                    num = num%100
                else:
                    ans+="D"
                    num = num%500
            elif(num >=100):
                if(num >=400):
                    ans+="CD"
                    num = num%100
                else:
                    ad = num//100
                    num = num%100
                    ans+=ad*"C"
            elif(num>=50):
                if(num >=90):
                    ans +="XC"
                    num = num%10
                else:
                    ans+="L"
                    num = num%50
            elif(num >=10):
                if(num >=40):
                    ans+="XL"
                    num = num%10
                else:
                    ad = num//10
                    num = num%10
                    ans+=ad*"X"
            elif(num>=5):
                if(num ==9):
                    ans +="IX"
                    num = 0
                else:
                    ans+="V"
                    num = num%5
            else:
                if(num ==4):
                    ans+="IV"
                    num = 0
                else:
                    ans+=num*"I"
                    num = 0
        return ans