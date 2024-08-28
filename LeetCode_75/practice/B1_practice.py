from typing import List

class MoveZeros:

    def moveZeros(self, nums: List[int]) -> List[int]:
        l = 0

        for r in range(1, len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        return nums

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    # Expected Output: [1,3,12,0,0]
    print(MoveZeros().moveZeros(nums=nums))
