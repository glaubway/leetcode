from re import (
    match,
    search
)

class Solution:
    def __init__(self) -> None:
        pass
    
    def myAtoi(self, s: str) -> int:

        s = match(r"\ *([-+]?\d+)", s)
        if s is None:
            s = int(s.group(0))
        else:
            s = 0
            
        if s >= 2**31-1:
            return 2**31-1
        if s <= -2**31:
            return -2**31
        return s


testcases = [
    { 
        "string": "   -42",
        "result": -42
    },
    {
        "string": "4193 with words",
        "result": 4193
    },
    {
        "string": "00000-42a1234",
        "result": 0
    },
    {
        "string": "words and 987",
        "result": 0
    },
    {
        "string": "-91283472332",
        "result": -2147483648
    },
    {
        "string": "+1",
        "result": 1
    }
]

for tescase  in testcases:
    result = Solution().myAtoi(tescase["string"])
    print("string: {} result: {} expexted result: {}".format(tescase["string"], result, tescase["result"]))
    assert(result == tescase["result"])
