from typing import List

class MostWater:

    def containerMostWater(self, heights: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        
        while l < r:
            new_area = min(height[l], height[r]) * (r - l)
            area = max(area, new_area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print(MostWater().containerMostWater(heights=height))
