def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        # since only lowercase english letters are used
        freq = [0]*26 # creating a list of 26 values with 0

        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1
        
        return all(f == 0 for f in freq)