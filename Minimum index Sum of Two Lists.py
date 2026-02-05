class Solution:
    def findRestaurant(self, list1, list2):
        d1 = {}
        d2 = {}
        for i,w in enumerate(list1):
            if(w not in d1):
                d1[w] = i
        for i,w in enumerate(list2):
            if(w not in d2):
                d2[w] = i
        min_ind = 10000000000
        ans = []
        for word in (set(list1) & set(list2)):
            if min_ind > d1[word]+d2[word]:
                min_ind = d1[word]+d2[word]
                ans = [word]
            elif(min_ind == d1[word]+d2[word]):
                ans.append(word)
        return ans
