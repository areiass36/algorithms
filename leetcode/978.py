from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        curGreater = 1
        maxGreater = 1
        curLower = 1
        maxLower = 1
        for i in range(1, len(arr)):
            if i % 2 == 0 and arr[i] > arr[i-1]:
                curGreater += 1
            elif i % 2 == 1 and arr[i] < arr[i-1]:
                curGreater += 1
            else:
                curGreater = 1
            maxGreater = max(curGreater, maxGreater)

        for i in range(1, len(arr)):
            if i % 2 == 0 and arr[i] < arr[i-1]:
                curLower += 1
            elif i % 2 == 1 and arr[i] > arr[i-1]:
                curLower += 1
            else:
                curLower = 1
            maxLower = max(curLower, maxLower)

        return max(maxGreater, maxLower)


number = Solution()
print(number.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))
