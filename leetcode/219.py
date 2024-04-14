from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        R = min(k, len(nums) - 1)
        looked = set()
        for L in range(0, len(nums)):
            if nums[L] in looked:
                return True
            looked.add(nums[L])
            if L == R:
                R = min(R + k, len(nums) - 1)
                looked.clear()
                looked.add(nums[R])
        return False


solution = Solution()
# [1,2,1],1
print(solution.containsNearbyDuplicate([1, 2, 1], 1))
