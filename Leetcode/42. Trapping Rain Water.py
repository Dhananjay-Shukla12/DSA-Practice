class Solution:
    def trap(self, height: list[int]) -> int:
        # sum = 0
        # prefixmax = []
        # suffixmax = []
        # prefixmax.append(height[0])
        # for i in range(1,len(height)):
        #     if height[i]>=prefixmax[i-1]:
        #         prefixmax.append(height[i])
        #     else:
        #         prefixmax.append(prefixmax[i-1])
        # n = len(height)
        # suffixmax.append(height[n-1])
        # j = 0
        # for i in range(n - 2, -1, -1):
        #     if height[i]>=suffixmax[j]:
        #         suffixmax.append(height[i])
        #     else:
        #         suffixmax.append(suffixmax[j])
        #     j+=1
        # suffixmax.reverse()

        # for i in range(1,len(height)):
        #     if height[i]<prefixmax[i] and height[i]<suffixmax[i]:
        #         sum+=min(prefixmax[i],suffixmax[i])-height[i]
        
        # return sum

        #two pointer approach

        sum = 0
        i = 0
        j = len(height)-1
        lmax = 0
        rmax = height[j]
        while i < j:
            if height[i]>lmax:
                lmax = height[i]
            if height[j]>rmax:
                rmax = height[j]
            if lmax <= rmax:
                sum += lmax-height[i]
                i+=1
            else:
                sum += rmax-height[j]
                j-=1
        return sum
            

            
