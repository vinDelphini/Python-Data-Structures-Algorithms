from itertools import zip_longest
class MergeStrings:

    def mergeStrings(self, word1: str, word2: str) -> str:
        return "".join(w1 + w2 for w1, w2 in zip_longest(word1, word2, fillvalue=''))


if __name__ == "__main__":
    word1 = "abcd"
    word2 = "pq"
    print(MergeStrings().mergeStrings(word1, word2))

    out = ""
    min_len = min(len(word1), len(word2))
    for i in range(min_len):
        out += word1[i] + word2[i]
    if len(word1) > len(word2):
        out += word1[min_len:]
    else:
        out += word2[min_len:]
    print(out)
