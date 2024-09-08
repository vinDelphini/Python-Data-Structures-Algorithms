from typing import List

class PivotIndex:

    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total_sum = sum(nums)
        for i in range(len(nums)):
            right_sum = total_sum - nums[i] - left_sum
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1


if __name__ == "__main__":
    nums = [1,7,3,6,5,6]
    # Expected Output: 3
    print(PivotIndex().pivotIndex(nums=nums))
