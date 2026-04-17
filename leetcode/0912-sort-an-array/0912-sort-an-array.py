class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr1,arr2):
            n1 = len(arr1)
            n2 = len(arr2)
            a = 0
            b = 0
            sor = []
            while(a < n1 and b < n2):
                if(arr1[a] < arr2[b]):
                    sor.append(arr1[a])
                    a+=1
                else:
                    sor.append(arr2[b])
                    b+=1
            while(a<n1):
                sor.append(arr1[a])
                a+=1
            while(b<n2):
                sor.append(arr2[b])
                b+=1
            return sor
        
        def merge_sort(left,right):
            if(left == right):
                return [nums[left]]
            
            mid = left+(right-left)//2
            left_sorted = merge_sort(left,mid)
            right_sorted = merge_sort(mid+1,right)

            return merge(left_sorted,right_sorted)
        
        return merge_sort(0,len(nums)-1)


    