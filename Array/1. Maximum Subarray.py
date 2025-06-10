def solution(nums):
    
    """ Kadane's Algorithm """

    # Required variables
    ans = 0
    result = float('-inf')

    # Main processing Logic
    for num in nums:
        ans += num
        result = max(result, ans)
        if ans < 0:
            ans = 0
    
    return result