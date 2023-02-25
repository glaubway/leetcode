class Solution:
    def __init__(self) -> None:
        pass
    
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 9:
            return True
        
        original = x
        reversed_num = 0

        while x > 0:
            reversed_num = reversed_num * 10 + (x % 10)
            x //= 10

        return original == reversed_num


testcases = [
    { 
        "string": 121,
        "result": True
    },
    {
        "string": -111,
        "result": False
    },
    {
        "string": 3,
        "result": True
    },
    {
        "string": 12,
        "result": False
    },
    {
        "string": 9876789,
        "result": True
    },
    {
        "string": +1,
        "result": True
    }
]

for tescase  in testcases:
    result = Solution().isPalindrome(tescase["string"])
    print("string: {} result: {} expexted result: {}".format(tescase["string"], result, tescase["result"]))
    assert(result == tescase["result"])
