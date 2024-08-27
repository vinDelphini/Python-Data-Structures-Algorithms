from typing import List

class IncreasingTriplet:

    def increasingTriplet(self, nums: List[int]) -> bool:
        num_i = float('inf')
        num_j = float('inf')
        for num in nums:
            if num <= num_i:
                num_i = num
            elif num <= num_j:
                num_j = num
            else:
                return True
        return False

if __name__ == "__main__":
    nums = [2,1,5,0,4,6]
    # Expected Output: true
    print(IncreasingTriplet().increasingTriplet(nums=nums))
