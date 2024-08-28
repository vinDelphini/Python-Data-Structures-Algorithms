from typing import List
class KSumPairs:

    def kSumPairs(self, nums: List[int], k:int) -> int:
        l, r = 0, len(nums) - 1
        count = 0
        while l < r:
            if nums[l] + nums[r] == k:
                l += 1
                r -= 1
                count += 1
            else:
                r -= 1
        return count


if __name__ == "__main__":
    nums = [1,2,3,4]
    k = 5
    # Expected Output: 2
    print(KSumPairs().kSumPairs(nums=nums, k=k))
