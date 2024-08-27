from typing import List

class MaxAvgSubarray:

    def maxAvgSubarray(self, nums: List[int], k: int) -> float:
        sum_sub = 0

        for i in range(k):
            sum_sub += nums[i]

        max_avg = sum_sub / k

        for i in range(k, len(nums)):
            sum_sub += nums[i]
            sum_sub -= nums[i - k]
            avg = sum_sub / k
            max_avg = max(max_avg, avg)
        return max_avg

if __name__ == "__main__":
    nums = [1,12,-5,-6,50,3]
    k = 4
    # expected output: 12.75000
    print(MaxAvgSubarray().maxAvgSubarray(nums=nums, k=k))
