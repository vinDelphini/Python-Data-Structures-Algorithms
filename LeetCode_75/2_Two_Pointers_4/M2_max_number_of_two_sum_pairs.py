from typing import List

class MaxNumberKSumPairs:

    def numberOfKSumPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        no_of_pairs = 0
        while l < r:
            current_sum = nums[l] + nums[r]
            if current_sum == k:
                no_of_pairs += 1
                l += 1
                r -= 1
            elif current_sum < k:
                l += 1
            else:
                r -=1

        return no_of_pairs


if __name__ == "__main__":
    nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
    k = 2
    # expected output: 2
    print(MaxNumberKSumPairs().numberOfKSumPairs(nums=nums, k=k))
