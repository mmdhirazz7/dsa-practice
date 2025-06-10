def chocolateDistribution(arr, m):

    n = len(arr)

    # Sorting the array
    arr.sort()

    minDiff = float("inf")
    
    for i in range(n-m+1):

        # Calculate the difference of the sliding window
        diff = arr[i+m-1] - arr[i]

        if diff < minDiff:
            minDiff = diff
    
    return minDiff

print(chocolateDistribution([2,4,100,3,4,586,84,20,30,40, 50, 33, 46, 78,90], 7))


