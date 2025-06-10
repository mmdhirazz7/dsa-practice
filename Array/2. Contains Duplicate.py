def ContainsDuplicates(nums):

    # Conversion of list to SET
    ans = set(nums)
        if len(ans) != len(nums):
            return True
        else:
            return False