from typing import List, Tuple

class RemoveElements:

    def removeElements(self, nums: List[int], val: int) -> Tuple[int, List[int]]:
        
        for i in nums:
            if i == val:
                nums.remove(i)
                nums.append("_")
        return nums

if __name__ == "__main__":

    nums = [0,1,2,2,3,0,4,2]
    val = 2
    # Output: 5, nums = [0,1,4,0,3,_,_,_]
    print(RemoveElements().removeElements(nums, val))