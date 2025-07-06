def encode(strs):
        encoded = []
        for s in strs:
            s_encd = str(len(s)) + "#" + s
            encoded.append(s_encd)
        return ''.join(encoded)
def decode(s):
    decoded = []
    i = 0
    while i < len(s):
        j = s[i:].index("#") + i
        length = int(s[i:j])
        word = s[j+1 : j+1+length]
        i = j + 1 +length
        decoded.append(word)
    return decoded

s = encode(["I", "am", "MD", "."])
print(s)
print(decode(s))  # Time complexity - O(L) & space complexity - O(n + L) where L is the sum of the lengths of all strings, N - noof strings.