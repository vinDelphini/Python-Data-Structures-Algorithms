from typing import List

class ClosestNumberToZero:

    def closestNumberToZero(self, nums: List[int]) -> int:

        neg_min_diff = float('-inf')
        pos_min_diff = float('inf')

        for i in nums:
            if i < 0:
                neg_min_diff = max(neg_min_diff, i)
            else:
                pos_min_diff = min(pos_min_diff, i)
        if -(neg_min_diff) == pos_min_diff or -(neg_min_diff) > pos_min_diff:
            return pos_min_diff
        else:
            return neg_min_diff
        


nums = [-4,-2, 0, 0, 1, 4,8]
# expected output: 1
print(ClosestNumberToZero().closestNumberToZero(nums))
