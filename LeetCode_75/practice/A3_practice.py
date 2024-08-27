from typing import List

class KidsWithCandies:

    def greatestCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        return [extraCandies + candy >= max_candy for candy in candies]
        

if __name__ == "__main__":
    candies = [2,3,5,1,3]
    extraCandies = 3
    # expected output: [true,true,true,false,true]
    print(KidsWithCandies().greatestCandies(candies=candies, extraCandies=extraCandies))
    