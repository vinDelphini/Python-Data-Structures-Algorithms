from typing import List

class MaximumAverageSubarray:

    def maxAvgSubarray(self, nums: List[int], k: int) -> float:
        sum_ = 0
        for i in range(k):
            sum_ += nums[i]

        avg_sum = sum_ / k

        for i in range(k, len(nums)):
            sum_ += nums[i]
            sum_ -= nums[i - k]
            new_avg = sum_ / k
            avg_sum = max(avg_sum, new_avg)
        
        return avg_sum
    

if __name__ == "__main__":
    nums = [1,12,-5,-6,50,3]
    k = 4
    # Expected Output: 12.75000
    print(MaximumAverageSubarray().maxAvgSubarray(nums=nums, k=k))