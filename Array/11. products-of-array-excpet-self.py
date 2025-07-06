def productExceptSelf(nums):
    # brute force
    # ans = []
    # for i in range(len(nums)):
    #     product = 1
    #     for j in range(len(nums)):
    #         if j == i:
    #             continue
    #         else:
    #             product *= nums[j]
    #     ans.append(product)
    # return ans

    # Optimized code [time complexity - O(n) & space complexity - O(1)]
    output = []
    output.append(1)
    for i in range(1,len(nums)):
        output.append(output[i-1]*nums[i-1])
    r = 1
    for i in range(len(nums)-1, -1, -1):
        output[i] *= r
        r *= nums[i]
    return output
print(productExceptSelf([1,2,3,4]))