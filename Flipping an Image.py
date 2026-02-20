class Solution:
    def flipAndInvertImage(self, image):
        m =len(image)
        n = len(image[0])
        for arr in image:
            left = 0
            right = n-1
            while(left<right):
                temp = arr[left]
                arr[left] = abs(arr[right]-1)
                arr[right] = abs(temp-1)
                left +=1
                right-=1
            if(left == right):
                arr[left] = abs(arr[right]-1)
        return image 