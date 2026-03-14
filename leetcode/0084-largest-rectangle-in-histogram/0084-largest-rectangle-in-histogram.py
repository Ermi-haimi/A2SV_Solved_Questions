class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        n = len(heights)
        st =[]
        mx_a = 0
        for i in range(n):
            start = i
            while(st and st[-1][0] >heights[i]):
                hei,ind = st.pop()
                wid = i-ind
                area = wid*hei
                mx_a = max(mx_a,wid*hei)
                start = ind
            st.append((heights[i],start))
        return mx_a
        