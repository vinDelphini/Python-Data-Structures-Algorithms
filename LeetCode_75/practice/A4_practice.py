from typing import List
class CanPlaceFlowers:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        flowerbed_ = [0] + flowerbed + [0]
        for i in range(len(flowerbed)):
            if flowerbed_[i - 1] == 0 and flowerbed_[i] == 0 and flowerbed_[i + 1] == 0:
                n -= 1
        
        if n <= 0:
            return True
        return False


if __name__ == "__main__":
    flowerbed = [1,0,0,0,1]
    n = 1
    # Expected Output: true
    print(CanPlaceFlowers().canPlaceFlowers(flowerbed=flowerbed, n=n))
