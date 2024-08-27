from typing import List


class MoveZeros:

    def moveZeros(self, nums: List[int]) -> List[int]:
        """moves all the zeros to the end of the list"""
        l = 0
        for i in range(len(nums)):
            # i will auto increment
            if nums[i] != 0:
                # only execute if i is not a 0
                nums[l], nums[i] = nums[i], nums[l]
                # increment if l is 0
                l += 1
        return nums


if __name__ == "__main__":

    nums = [0,1,0,3,12]
    # expected output: [1,3,12,0,0]
    print(MoveZeros().moveZeros(nums=nums))
