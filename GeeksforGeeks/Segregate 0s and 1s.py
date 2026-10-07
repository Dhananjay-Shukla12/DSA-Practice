class Solution:
    def segregate0and1(self, arr):
        #using count
            
            # zer = arr.count(0)
            # one = arr.count(1)
            
            # i = 0
            # while zer!=0:
            #     arr[i] = 0
            #     i+=1
            #     zer-=1
            # while one!=0:
            #     arr[i]=1
            #     i+=1
            #     one-=1
        
        #using Sort
            
            # arr.sort()
            
        
        #using two pointer
            
            i = 0
            j = len(arr)-1
            while i<j:
                if arr[i] == 1 and arr[j] == 0:
                    t = arr[i]
                    arr[i] = arr[j]
                    arr[j] = t
                    i+=1
                    j-=1
                elif arr[i] == 0:
                    i+=1
                elif arr[j] == 1:
                    j-=1
                else:
                    i+=1
            
            
        
        
        
        