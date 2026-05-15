class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sm = []
        an = len(a)
        bn = len(b)
        ai = an-1
        bi = bn-1
        carry = 0
        while(ai>=0 and bi>=0):
            if(a[ai] =='1'):
                if(b[bi]=='1'):
                    if(carry == 1):
                        sm.append("1")
                    else:
                        sm.append("0")
                        carry=1
                else:
                    if(carry == 1):
                        sm.append("0")
                    else:
                        sm.append("1")
            else:
                if(b[bi]=='1'):
                    if(carry == 1):
                        sm.append("0")
                    else:
                        sm.append("1")
                else:
                    if(carry == 1):
                        sm.append("1")
                        carry = 0
                    else:
                        sm.append("0")
            ai-=1
            bi-=1
        while(ai>=0):
            if(a[ai]=="1"):
                if(carry ==1):
                    sm.append('0')
                else:
                    sm.append('1')
            else:
                if(carry ==1):
                    sm.append('1')
                    carry=0
                else:
                    sm.append('0')
            ai-=1
        while(bi>=0):
            if(b[bi]=="1"):
                if(carry ==1):
                    sm.append('0')
                else:
                    sm.append('1')
            else:
                if(carry ==1):
                    sm.append('1')
                    carry=0
                else:
                    sm.append('0')
            bi-=1


        if carry == 1:
            sm.append("1")
        sm.reverse()
        return "".join(sm)

        