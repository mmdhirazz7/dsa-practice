def isPalindrome(s):

    """Code is written based on the cost effectiveness."""

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        elif s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        elif not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        else:
            return False
    return True

print(isPalindrome("..ab..ab"))