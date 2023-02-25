from typing import List


class Solution:
    def __init__(self) -> None:
        pass
    
    def convert(self, s: str, numRows: int) -> str:
        charRows: List[str] =  [ '' for _ in range(numRows) ]
        if numRows == 1:
            return s

        rowIndex:int = 0
        direction: int = 1
        for stringIndex in range(len(s)):

            charRows[rowIndex] += s[stringIndex]

            if rowIndex == numRows -1:
                direction = -1
            elif rowIndex == 0:
                direction = 1

            rowIndex += direction

        return "".join(charRows)



testcases = [
    { 
        "string": "PAYPALISHIRING",
        "rows": 3,
        "result": "PAHNAPLSIIGYIR"
    },
    {
        "string":  "PAYPALISHIRING",
        "rows": 4,
        "result": "PINALSIGYAHRPI"
    },
    {
        "string":  "ABCA",
        "rows": 2,
        "result": "ACBA"
    },
    {
        "string":  "A",
        "rows": 1,
        "result": "A"
    }
]

for tescase  in testcases:
    result = Solution().convert(tescase["string"], tescase["rows"])
    print("string: {} rows: {} result: {} expexted result: {}".format(tescase["string"], tescase["rows"], result, tescase["result"]))
    assert(result == tescase["result"])
