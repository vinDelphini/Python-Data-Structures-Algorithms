from typing import List

class MergeArrays:

    def mergeSortedArrays(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        for i in range(m, len(nums1)):
            nums1[i] = nums2[i - m]
        nums1.sort()
        return nums1


if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    # Expected Output: [1,2,2,3,5,6]
    print(MergeArrays().mergeSortedArrays(nums1=nums1, m=m, nums2=nums2, n=n))
