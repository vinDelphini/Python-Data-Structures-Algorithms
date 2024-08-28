from typing import List
from collections import Counter


class UniqueOccurances:

    def uniqueOccurances(self, arr: List[int]) -> bool:
        
        arr_dict = Counter(arr)
        return len(arr_dict.values()) == len(set(arr_dict.values()))


if __name__ == "__main__":
    arr = [1,2,2,1,1,3]
    # Expected Output: true
    print(UniqueOccurances().uniqueOccurances(arr=arr))
