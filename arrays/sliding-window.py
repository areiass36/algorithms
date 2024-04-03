def slidingWindow(array: [int], k: int):
    L = 0
    R = min(k, len(array) - 1)
    looked = set()
    while L < len(array):
        print(R)
        if array[L] in looked:
            return True
        looked.add(array[L])
        L += 1
        if L == R:
            R += k 
            looked.clear()
    return False


print(slidingWindow([1, 2, 4, 0, 4, 5], 2))
