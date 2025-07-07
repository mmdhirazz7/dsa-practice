def longestConsecutiveSequence(nums):

    """ Brute force approach takes O(n^3), 
    but this algorithm, having analyzed in the amortized approach, takes O (N) approach ."""
    
    max_count = 0

    freq = set()
    for num in nums:
        freq.add(num)

    for num in freq:
        current_num = num
        count = 1
        if num - 1 not in freq:
            while current_num + 1 in freq:
                current_num += 1
                count += 1
        if max_count < count:
            max_count = count

    return max_count

print(longestConsecutiveSequence([2,3,100,34,5,3,4,7,6]))