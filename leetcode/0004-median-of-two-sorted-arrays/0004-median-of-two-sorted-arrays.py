class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        tot = len(nums1)+len(nums2)
        half = tot//2 
        if(len(nums1) > len(nums2)):
            A = nums2
            B = nums1

        l = 0
        r = len(A)-1
        while(True):
            midA = l+(r-l)//2
            midB = half-midA-2

            leftA = A[midA] if midA>=0 else float("-infinity")
            rightA = A[midA+1] if midA+1<len(A) else float("infinity")
            leftB = B[midB] if midB>=0 else float("-infinity")
            rightB = B[midB+1] if midB+1<len(B) else float("infinity")

            if(leftA <= rightB and leftB <= rightA):
                if(tot%2 ==0):
                    return (max(leftA, leftB)+min(rightA,rightB))/2
                return min(rightA, rightB)
            elif(leftA>rightB):
                r=midA-1
            else:
                l = midA+1
            


            
        
