from typing import List

class RemoveElement:
    
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index


if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    # Expected Output: 1, nums = [2]
    print(RemoveElement().removeElement(nums=nums, val=val))
