from collections import deque


def slidingWindow(nums: [int], k: int):
    if k == 0:
        return False
    queue = deque()
    R = k
    for L in range(0, len(nums)):
        cur = nums[L]
        print(queue)
        if L == R:
            R += k
            queue.popleft()
        if cur in queue:
            return True
        queue.append(cur)
    return False


print(slidingWindow([1, 2, 3, 1], 3))
print(slidingWindow([1, 0, 1, 1], 1))
print(slidingWindow([1, 2, 3, 1, 2, 3], 2))
print(slidingWindow([4, 1, 2, 3, 1, 5], 2))
