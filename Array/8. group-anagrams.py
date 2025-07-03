def groupAnagrams(strs):
        """Given a list of strings, group all anagrams together into a sublist, you can return the output in any order."""
        """O(n * klogk) approach"""
        # anagram_map = {}

        # for s in strs:
        #     key = ''.join(sorted(s))
        #     if key not in anagram_map:
        #         anagram_map[key] = []
        #     anagram_map[key].append(s)

        # return list(anagram_map.values())

        """O(m*n) m = len(arr), n = max(len(any string))"""
        anagram_map = {}
        for s in strs:
            count = [0]*128
            for c in s:
                count[ord(c)] += 1
            key = tuple(count)
            if key not in anagram_map:
                anagram_map[key] = []
            anagram_map[key].append(s)
        return list(anagram_map.values())

print(groupAnagrams(["", " "]))
