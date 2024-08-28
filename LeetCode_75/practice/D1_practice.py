from typing import List

class HighestAltitude:

    def highestAlt(self, gain: List[int]) -> int:
        
        max_alt = 0
        alt = 0
        for i in gain:
            alt += i
            max_alt = max(max_alt, alt)
        return max_alt

gain = [-5,1,5,0,-7]
# Expected Output: 1)
print(HighestAltitude().highestAlt(gain))
