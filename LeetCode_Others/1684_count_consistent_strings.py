from typing import List

class ConsistentStrings:

    def countConsistentStrings(self, allowed: str, words:List[str]) -> int:
        
        allowed = set(allowed)  # Convert to set for O(1) lookups

        def isConsistent(word):
            for letter in word:
                if letter not in allowed:
                    return False
            return True
        
        count = 0

        for word in words:
            if isConsistent(word):
                count += 1

        return count
        # return sum(set(word).issubset(allowed) for word in words)


if __name__ == "__main__":
    allowed = "abc"
    words = ["a","b","c","ab","ac","bc","abc"]
    # Expected Output: 7
    cs1 = ConsistentStrings()
    print(cs1.countConsistentStrings(allowed=allowed, words=words))
