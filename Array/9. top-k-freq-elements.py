def topKFrequent(nums, k):
        
        # sorting - based approach 
        # mode = {}

        # for num in nums:
        #     mode[num] = mode.get(num, 0) + 1
        
        # modeOrdered = {k : v for k, v in sorted(mode.items(), key=lambda item:-item[1])}
        # search = list(modeOrdered.keys())
        # ans = []
        # for i in range(k):
        #     ans.append(search[i])
        # return ans

        # more efficient one O(n)
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # creating a buckets array
        buckets = []
        for i in range(len(nums)+1):
            buckets.append([])
        
        # Storing the modes in the buckets
        for key in freq.keys():
            buckets[freq[key]].append(key)
        
        # Retrieving the k modes
        ans = []
        for j in range(len(buckets)-1, -1,-1):
            if len(buckets) == 1 and k > 0:
                ans.append(buckets[j][0])
                k -= 1
            elif len(buckets) > 1:
                for i in range(len(buckets[j])):
                    if k > 0:
                        ans.append(buckets[j][i])
                        k -= 1
        return ans

print(topKFrequent([1,1,1,2,2,2,3,3,3,4,4,4], 3))