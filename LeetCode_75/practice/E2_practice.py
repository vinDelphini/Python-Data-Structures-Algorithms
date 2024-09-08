from typing import List
from collections import Counter

class UniqueOccurances:

    def uniqueOccurances(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        return len(set(counts.values())) == len(counts.values())


if __name__ == "__main__":
    arr = [1,2,2,1,1,3]
    # Expected Output: true
    print(UniqueOccurances().uniqueOccurances(arr=arr))
