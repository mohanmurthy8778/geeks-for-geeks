
class Solution:
    def missingNum(self, arr):
        arr.sort()
        n = arr[-1]
        
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1
        
        return n + 1
