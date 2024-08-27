from itertools import zip_longest

class MergeStrings:

    def mergeAlternatively(self, word1: str, word2: str) -> str:
        return "".join(w1 + w2 for w1, w2 in zip_longest(word1, word2, fillvalue=""))

word1 = "abc"
word2 = "pqr"
# Expected Output: "apbqcr"
print(MergeStrings().mergeAlternatively(word1=word1, word2=word2))
