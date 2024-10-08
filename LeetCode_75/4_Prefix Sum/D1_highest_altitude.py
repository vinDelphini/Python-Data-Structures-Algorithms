from typing import List

class HighestAltitude:

    def highestAltitude(self, gain: List[int]) -> int:
        alt = 0
        max_alt = 0
        for i in gain:
            alt += i
            max_alt = max(max_alt, alt)
        return max_alt


if __name__ == "__main__":
    gain = [-4,-3,-2,-1,4,3,2]
    print(HighestAltitude().highestAltitude(gain=gain))
    # expected output: 0