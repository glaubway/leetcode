class Solution:
    def __init__(self) -> None:
        pass

    def lengthOfLongestSubstring(self, s: str) -> int:
        nonRepeatLen: int = 0
        substring: str = ""

        for char in s:
            if char in substring:
                substring = substring[substring.index(char)+1:]
                
            substring += char
            nonRepeatLen = max(nonRepeatLen, len(substring))
        return nonRepeatLen


testcases = {
    "aab" : 2,
    "bbbbb": 1,
    "aaabcdefaas": 6,
    "123asdcxa": 8,
    "abcabcbb": 3,
    "dvdf": 3,
    "ckilbkd": 5
}

for string, expresult in testcases.items():
    result = Solution().lengthOfLongestSubstring(string)
    print(f"string: {string} result: {result} expexted result: {expresult}")
    assert(result == expresult)
