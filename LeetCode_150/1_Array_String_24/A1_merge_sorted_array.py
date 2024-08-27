from typing import List

class MergeSortedArray:
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges 2 sorted Arrays of integers with length m & n
        """
        for i in range(m, len(nums1)):
            nums1[i] = nums2[i - m]
        nums1.sort()
        return nums1

if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(MergeSortedArray().merge(nums1=nums1, m=m, nums2=nums2, n=n))
