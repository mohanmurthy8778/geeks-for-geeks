class Solution:
    def getSecondLargest(self, arr):
        first = -1
        second = -1

        for num in arr:
            if num > first:
                second = first
                first = num
            elif second < num and num != first:
                second = num

        return second
