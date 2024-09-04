from typing import List


class ConvertArray:

    def convertArrays(self, original: List[int], m: int, n:int) -> List[List[int]]:
        out =[]

        for i in range(0, len(original), n):
            if m * n == len(original):
                out.append(original[i : i + n])
        return out 


if __name__ == "__main__":
    original = [1,2,3,4]
    m = 2
    n = 2
    # Expected Output: [[1,2],[3,4]]

    print(ConvertArray().convertArrays(original=original, m=m, n=n))
