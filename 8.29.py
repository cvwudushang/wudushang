import numpy as np
class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        dp=np.zeros(len(arr))
        for i in range(len(arr)):
            temp=self.findlr(arr,i)

        #print(dp)
    def findlr(self,arr,i):
        temp=np.zeros()
        l=0
        for j in range(i):
            for k in range(i):
                if arr[j]*arr[k]==arr[i]:
                    temp[l]=j
                    temp[l]=k
                    l+=1
        return
arr=[2,4,5,10]
a=Solution()
a.numFactoredBinaryTrees(arr)
len(arr)