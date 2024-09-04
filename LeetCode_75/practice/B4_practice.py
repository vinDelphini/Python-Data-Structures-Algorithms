from typing import List

class MaxKSumPairs:
    
    def kSumPairs(self, nums: List[int], k: int) -> int:
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
                r -= 1
        return no_of_pairs


if __name__ == "__main__":
    nums = [3,1,3,4,3]
    k = 6

    # Expected Output: 1
    print(MaxKSumPairs().kSumPairs(nums=nums, k=k))
