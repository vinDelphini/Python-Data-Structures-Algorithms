from typing import List
from collections import Counter
class UniqueOccurrences:

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_ = Counter(arr)
        return len(set(dict_.values())) == len(dict_.values())
        



if __name__ == "__main__":

    arr = [8,9,9,8,8,10]
    # expected output: true
    print(UniqueOccurrences().uniqueOccurrences(arr))