from typing import List

class TripletSequence:

    def tripletSequence(self, nums: List[int]) -> bool:
        l = 0
        count = 1
        for r in range(1, len(nums)):
            if nums[l] < nums[r]:
                count += 1
            else:
                l += 1
        return count



if __name__ == "__main__":
    nums = [4,5,1,2,3]
    # Expected Output: true
    print(TripletSequence().tripletSequence(nums=nums))