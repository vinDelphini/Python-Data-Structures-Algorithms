from typing import List
class CanPlaceFlowers:
    
    def placeFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed_ = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed) + 1):
            if flowerbed_[i - 1] == 0 and flowerbed_[i] == 0 and flowerbed_[i + 1] == 0:
                flowerbed_[i] = 1
                n -= 1
        return n <= 0





if __name__ == "__main__":
    flowerbed = [1,0,0,0,1,0,0]
    n = 2
    # Output: true
    print(CanPlaceFlowers().placeFlowers(flowerbed=flowerbed, n=n))
