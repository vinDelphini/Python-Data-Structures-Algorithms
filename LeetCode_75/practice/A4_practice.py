from typing import List

class CanPlaceFlowers:

    def canPlaceFlowers(self, flowerbed: List[int], n:int) -> bool:
        flowerbed_ = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) + 1):
            if flowerbed_[i - 1] == 0 and flowerbed_[i] == 0 and flowerbed_[i + 1] == 0:
                n -= 1
        return n <= 0


if __name__ == "__main__":
    flowerbed = [1,0,0,0,1]
    n = 1
    # expected output: true
    print(CanPlaceFlowers().canPlaceFlowers(flowerbed=flowerbed, n=n))
