from typing import List


class DivisibleByThree:

    def divByThree(self, nums: List[int]) -> int:
        
        count = 0
        for num in nums:
            if num % 3 != 0:
                count += 1
        # return count

        return sum([num % 3 != 0 for num in nums])
    
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    # Expected Output: 3
    print(DivisibleByThree().divByThree(nums=nums))
    
    # Solution 2
    from collections import Counter
    nums_ = [num %3 for num in nums]
    ctr =  Counter(nums_)
    print(ctr[1] + ctr[2])

    # Solution 3
    num = sum(map(lambda x: x % 3 != 0, nums))
    print(num)

    # Solution 4 (BEST SOLUTION)
    print(sum(1 for num in nums if num % 3 != 0))
