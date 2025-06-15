def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # Finding the next lexicographical permutation

        # sort the array
        # nums.sort()

        # Define the piv0t index
        pivot = -1

        # Permutaions
        # permutations = [nums]

        # Creating next permutations
        #initializing iterator index i
        i = len(nums) - 2
        while i >= 0:
            
            if nums[i] < nums[i+1]:
                pivot = i

                # swap the pivot element and the last element
                max_i = len(nums)-1
                for j in range(len(nums)-1, i, -1):
                    if nums[j] > nums[i]:
                        max_i = j
                        break
                nums[pivot], nums[max_i] = nums[max_i], nums[pivot]
                nums[pivot+1:] = sorted(nums[pivot+1:])
                # permutations.append(nums)
                return nums
                i = len(nums) - 2
            else:
                i -= 1
        return nums.sort()