from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) <=1:
            return s

        newString = "|".join(f"#{s}#")
        stringLen = len(newString)
        palindromeArray: List[int] = [0] * stringLen
        center:int = 0
        radius:int = 0
        for index in range(1, stringLen-1):
            indexMirror:int = 2 * center - index
            if radius > index:
                palindromeArray[index] = min(radius - index, palindromeArray[indexMirror])
            else:
                palindromeArray[index] = 0
            try:
                while newString[index + 1 + palindromeArray[index]] == newString[index - 1 - palindromeArray[index]]:
                    palindromeArray[index] += 1
            except IndexError:
                pass
            if index + palindromeArray[index] > radius:
                center = index
                radius = index + palindromeArray[index]
        max_len, center_index = max((palindromeArray[index], index) for index in range(1, stringLen-1))
        return s[(center_index - max_len)//2:(center_index + max_len)//2]



testcases = [
    { 
        "string": "babad",
        "result": "aba"
    },
    {
        "string":  "aassaad",
        "result": "aassaa"
    },
    {
        "string":  "cbbd",
        "result": "bb"
    }
]

for tescase  in testcases:
    result = Solution().longestPalindrome(tescase["string"])
    print("string: {} result: {} expexted result: {}".format(tescase["string"], result, tescase["result"]))
    assert(result == tescase["result"])
