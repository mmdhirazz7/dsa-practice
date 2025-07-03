def twoSum(nums, target):
    """ Takes the list of integers and a target number, 
    and returns the indices of the list in the order they are stored in the list 
    whose values add up to target"""
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