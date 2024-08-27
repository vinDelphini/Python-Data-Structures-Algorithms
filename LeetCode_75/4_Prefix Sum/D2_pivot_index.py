from typing import List


class PivotIndex:

    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1


if __name__ == "__main__":
    nums = [1,7,3,6,5,6]
    # expected output: 3
    print(PivotIndex().pivotIndex(nums=nums))
