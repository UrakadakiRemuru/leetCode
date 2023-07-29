from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        tmp = 0
        listRes = []
        for i, val in enumerate(nums):
            tmp += val
            listRes.append(tmp)
        return listRes