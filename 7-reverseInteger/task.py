class Solution:
    def __init__(self) -> None:
        pass
    
    def reverse(self, x: int) -> int:
        rev_x = int(str(abs(x))[::-1])

        if rev_x.bit_length() < 32:
            if x > 0:
                return rev_x
            return -rev_x
        return 0

testcases = [
    { 
        "string": 123,
        "result": 321
    },
    {
        "string": 321,
        "result": 123
    },
    {
        "string": -123,
        "result": -321
    },
    {
        "string": 120,
        "result": 21
    },
    {
        "string": 1534236469,
        "result": 0
    }
]

for tescase  in testcases:
    result = Solution().reverse(tescase["string"])
    print("string: {} result: {} expexted result: {}".format(tescase["string"], result, tescase["result"]))
    assert(result == tescase["result"])
