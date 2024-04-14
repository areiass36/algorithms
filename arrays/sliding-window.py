def slidingWindow(nums: [int], k: int):
    map = {}
    for i in range(len(nums)):
        cur = nums[i]
        if cur in map and abs(i - map[cur]) <= k:
            return True
        map[cur] = i
    return False


print(slidingWindow([1, 2, 3, 1], 3))
print(slidingWindow([1, 0, 1, 1], 1))
print(slidingWindow([1, 2, 3, 1, 2, 3], 2))
print(slidingWindow([4, 1, 2, 3, 1, 5], 3))
