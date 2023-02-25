from typing import List

class Solution:
    def __init__(self) -> None:
        pass

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median: int = 0
        merged_list: list = sorted(nums1 + nums2)
        listlen: int = len(merged_list)
        index: int = (listlen - 1)//2
        if listlen % 2 == 0:
            median = (merged_list[index] + merged_list[index+1])/2
        else:
            median = merged_list[index]
        return median


testcases = [
    {
        "nums1": [1, 3],
        "nums2": [2],
        "result": 2
    },
    {
        "nums1": [1, 2],
        "nums2": [3, 4],
        "result": 2.5
    }
]

for tescase  in testcases:
    result = Solution().findMedianSortedArrays(tescase["nums1"], tescase["nums2"])
    print("num1: {} num2: {} result: {} expexted result: {}".format(tescase["nums1"], tescase["nums2"], result, tescase["result"]))
    assert(result == tescase["result"])
