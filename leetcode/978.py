from typing import List

# https://leetcode.com/problems/longest-turbulent-subarray/
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        curGreater = 1
        maxGreater = 1
        curLower = 1
        maxLower = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                if i % 2 == 0:
                    curGreater += 1
                    curLower = 1
                else:
                    curLower += 1
                    curGreater = 1
            elif arr[i] < arr[i-1]:
                if i % 2 == 0:
                    curLower += 1
                    curGreater = 1
                else:
                    curLower = 1
                    curGreater += 1
            else:
                curLower = 1
                curGreater = 1

            maxGreater = max(curGreater, maxGreater)
            maxLower = max(curLower, maxLower)

        return max(maxGreater, maxLower)

    def maxTurbulenceSize2(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        flag = arr[0] > arr[1]
        curSum = 2 if arr[0] != arr[1] else 1
        maxSum = curSum

        for i in range(2, len(arr)):
            curFlag = arr[i-1] > arr[i]
            if flag ^ curFlag and arr[i] != arr[i-1]:
                curSum += 1
            else:
                curSum = 2 if arr[i] != arr[i-1] else 1
            maxSum = max(curSum, maxSum)
            flag = curFlag
        return maxSum


number = Solution()
print(number.maxTurbulenceSize2())
