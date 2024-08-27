from typing import List

class DifferenceOfTwoArrays:

    def diffTwoArrays(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res1 = set()
        res2 = set()

        for i in nums1:
            if i not in nums2:
                res1.add(i)
        
        for i in nums2:
            if i not in nums1:
                res2.add(i)
        
        return [list(res1), list(res2)]
    

if __name__ == "__main__":
    nums1 = [1,2,3]
    nums2 = [2,4,6]
    # Expected Output: [[1,3],[4,6]]
    print(DifferenceOfTwoArrays().diffTwoArrays(nums1=nums1, nums2=nums2))
