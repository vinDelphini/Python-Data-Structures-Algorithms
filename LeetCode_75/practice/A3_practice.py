from typing import List
class KidsWithCandies:

    def greatestNumberCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        return [extraCandies + candy >= maxCandy for candy in candies]


if __name__ == "__main__":
    candies = [2,3,5,1,3]
    extraCandies = 3
    # Expected Output: [true,true,true,false,true] 
    print(KidsWithCandies().greatestNumberCandies(candies=candies, extraCandies=extraCandies))
