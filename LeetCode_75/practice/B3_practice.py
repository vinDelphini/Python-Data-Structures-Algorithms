from typing import List
class MostWaterContainer:

    def mostWater(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            min_height = min(height[l], height[r])
            distance = r - l
            area = min_height * distance

            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area



if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    # Expected Output: 49
    print(MostWaterContainer().mostWater(height=height))
