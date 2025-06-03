class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = ''.join([char for char in s if char.isalnum()])
        return True if valid[::-1].lower() == valid.lower() else False
        

sol = Solution()
res = sol.isPalindrome("race a car")
print(res)