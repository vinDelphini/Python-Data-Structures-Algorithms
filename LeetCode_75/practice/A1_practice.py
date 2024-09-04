from itertools import zip_longest

class mergeAlternateStr:

    def mergeStrings(self, word1: str, word2: str) -> str:
        return "".join(w1 + w2 for w1, w2 in zip_longest(word1, word2, fillvalue=""))

if __name__ == "__main__":
    word1 = "abc"
    word2 = "pqr"
    # Expected Output: "apbqcr"
    print(mergeAlternateStr().mergeStrings(word1=word1, word2=word2))
