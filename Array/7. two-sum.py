def twoSum(nums, target):
    """ Finds two distinct indices in the input list such that the sum of the corresponding values equals the target.
    
    parameters : 
                nums (List[int]) : a list of integers
                target (int) : the target sum to find.
    returns :
        List[int] : A List containing two indices [i,j] where nums[i] + nums[j] == target, and i < j"""

    # Brute force method
    # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             result[0] = i
        #             result[1] = j
        # return result
        
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen :
            return [seen[target-num], i]
        else:
            seen[num] = i

print(twoSum([3,2,3], 6))