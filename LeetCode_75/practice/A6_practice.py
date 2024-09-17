class ReverseWordsString:

    def reverseWordsString(self, s: str) -> str:
        return " ".join(reversed(s.strip().split()))


if __name__ == "__main__":
    s = "the sky is blue"
    # Expected Output: "blue is sky the"
    print(ReverseWordsString().reverseWordsString(s))