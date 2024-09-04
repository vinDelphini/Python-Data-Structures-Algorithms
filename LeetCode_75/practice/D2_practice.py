from typing import List


class PivotIndex:

    def pivotIndex(self, nums: List[int]) -> int:

        total = sum(nums)

        left_sum = 0
        right_sum = 0

        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1
    
    
if __name__ == "__main__":
    nums = [1,7,3,6,5,6]
    # Expected Output: 3
    print(PivotIndex().pivotIndex(nums=nums))
