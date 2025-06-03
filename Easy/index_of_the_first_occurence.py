class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        print(len(haystack))

        for i in range(len(haystack) - len(needle) + 1):  
            str1 = haystack[i:i+len(needle)]
            if str1 == needle:
                return i 

        return index  


sol = Solution()
res = sol.strStr("aaaaaaab", "aaab")
print(res)
