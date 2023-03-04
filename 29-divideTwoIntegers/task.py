class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return None
        if dividend == 0:
                return 0
        positive = (dividend > 0) is (divisor > 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        remainder = 0

        for i in range(31, -1, -1):
            if remainder + (divisor << i) <= dividend:
                remainder += divisor << i
                quotient |= 1 << i

        if positive and quotient >= 2**31-1:
            return 2**31-1
        if quotient <= -2**31:
            return -2**31

        return quotient if positive else -quotient
    


testcases = [
    { 
        "dividend": 10,
        "divisor": 3,
        "result": 3
    },
    { 
        "dividend": 7,
        "divisor": -3,
        "result": -2
    },
    { 
        "dividend": -2147483648,
        "divisor": -1,
        "result": 2147483647
    },
]

for tescase  in testcases:
    result = Solution().divide(tescase["dividend"], tescase["divisor"])
    print("dividend: {} divisor: {} result: {} expexted result: {}".format(tescase["dividend"], tescase["divisor"], result, tescase["result"]))
    assert(result == tescase["result"])
