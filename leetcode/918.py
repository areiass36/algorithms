from typing import List

# https://leetcode.com/problems/maximum-sum-circular-subarray/

# kadane
def maxSubarraySumCircular(nums: List[int]) -> int:
    curMaxSum = 0
    maxSum = nums[0]

    curMinSum = 0
    minSum = nums[0]

    sum = 0
    for n in nums:
        sum = sum + n
        curMaxSum = max(n, curMaxSum + n)
        curMinSum = min(n, curMinSum + n)
        maxSum = max(maxSum, curMaxSum)
        minSum = min(minSum, curMinSum)

    return maxSum if maxSum < 0 else max(maxSum, sum - minSum)
