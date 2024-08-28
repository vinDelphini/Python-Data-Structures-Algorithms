from typing import List


class MaximumAverageSubarray:

    def maximumAvgSubarray(self, nums: List[int], k: int):
        l = len(nums)
        sum = 0

        for i in range(k):
            sum += nums[i]

        max_avg = sum / k

        for i in range(k, l):
            sum -= nums[i - k]
            sum += nums[i]
            avg = sum / k
            max_avg = max(max_avg, avg)
        
        return max_avg


if __name__ == "__main__":
    nums = [1,12,-5,-6,50,3]
    k = 4
    # Expected Output: 12.75000
    print(MaximumAverageSubarray().maximumAvgSubarray(nums=nums, k=k))
