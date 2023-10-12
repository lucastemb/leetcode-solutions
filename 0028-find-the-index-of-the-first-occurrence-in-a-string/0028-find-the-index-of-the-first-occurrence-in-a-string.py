class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            for j in range(len(needle)):
                if (i+j) >= len(haystack):
                    return -1
                if haystack[i+j] != needle[j]:
                    break
            if j == len(needle)-1 and needle[j] == haystack[i+j]:
                return i
        return -1
