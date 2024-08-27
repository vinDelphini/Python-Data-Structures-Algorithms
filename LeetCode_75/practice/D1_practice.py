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
    gain = [-5,1,5,0,-7]
    # expected output: 1
    print(HighestAltitude().highestAltitude(gain=gain))
