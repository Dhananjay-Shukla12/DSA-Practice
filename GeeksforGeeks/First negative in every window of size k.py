class Solution:
    def firstNegInt(self, arr, k): 
         # code here 
         q=[]
         i=0
         j=0
         ans=[]
         
         while j<len(arr):
             if arr[j]<0:
                 q.append(arr[j])
             if (j-i+1) < k:
                j+=1
             elif (j-i+1)==k:
                if len(q)==0:
                    ans.append(0)
                else:
                    ans.append(q[0])
                    if q[0]==arr[i]:
                        q.pop(0)
                i+=1
                j+=1
         return ans
