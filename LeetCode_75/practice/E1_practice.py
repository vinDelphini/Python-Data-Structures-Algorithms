from typing import List

class DifferenceTwoArrays:

    def differenceTwoArrays(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    
        out1 = set()
        out2 = set()
    
        for i in nums1:
            if i not in nums2:
                out1.add(i)
        
        for i in nums2:
            if i not in nums1:
                out2.add(i)
        
        return [list(out1), list(out2)]

if __name__ == "__main__":
    nums1 = [1,2,3]
    nums2 = [2,4,6]
    # Expected Output: [[1,3],[4,6]]
    print(DifferenceTwoArrays().differenceTwoArrays(nums1=nums1, nums2=nums2))
