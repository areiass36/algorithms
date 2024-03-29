def kadane(array):
    maxSum = array[0]
    curSum = 0

    for i in range(1, len(array)):
        # reset curSum if it is less than 0
        curSum = max(array[i], curSum + array[i])
        maxSum = max(maxSum, curSum)

    return maxSum
