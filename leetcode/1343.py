from typing import List


class Solution:
    # First solution O(n*k) time complexity
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        for L in range(0, len(arr) - k + 1):
            sum = 0
            for R in range(L, L + k):
                sum += arr[R]
            if (sum / k) >= threshold:
                count += 1
        return count

    # Second try O(n)
    def numOfSubarrays2(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0
        count = 0
        map = {}
        for i in range(len(arr) - 1, -1, -1):
            total += arr[i]
            map[i] = total
        curSum = 0
        for i in range(0, len(arr) - k + 1):
            windowSum = total - curSum
            if i < len(arr) - k:
                windowSum -= map[i+k]
            if windowSum / k >= threshold:
                count += 1
            curSum += arr[i]
        return count

    # Solution found on leetcode
    def numOfSubarrays3(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        res = 0
        sum_ = sum(arr[:k])

        for i in range(k, n):
            if sum_ / k >= threshold:
                res += 1
            sum_ += arr[i] - arr[i - k]

        # Check the last window after the loop
        if sum_ / k >= threshold:
            res += 1

        return res


sol = Solution()
# print(sol.numOfSubarrays2([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))
print(sol.numOfSubarrays2([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5))
