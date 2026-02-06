from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains):
        domains = defaultdict(int)
        for domain in cpdomains:
            space = domain.find(" ")
            visits = int(domain[:space])
            site = domain[space+1:]
            last = -1
            while(site[:last].rfind(".") > -1):
                dot = site[:last].rfind(".")
                domains[site[dot+1:]]+=visits
                last = dot
            domains[site]+=visits
        ans = []
        for key, item in domains.items():
            ans.append(str(item) + " " + key)
        
        return ans