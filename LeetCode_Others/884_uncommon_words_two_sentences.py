from collections import Counter
from typing import List

class UncommonWords:

    def uncommonWords(self, s1: str, s2: str) -> List[str]:
        s3 = Counter(s1.split() + s2.split())
        return [key for key, value in s3.items() if value == 1]

if __name__ == "__main__":
    s1 = "this apple is sweet"
    s2 = "this apple is sour"
    print(UncommonWords().uncommonWords(s1, s2))
