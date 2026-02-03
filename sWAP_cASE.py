def swap_case(s):
    ans = ""
    for c in s:
        if c.isalpha():
            if(c.isupper()):
                ans+=c.lower()
            else:
                ans+=c.upper()
        else:
            ans+=c
    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)