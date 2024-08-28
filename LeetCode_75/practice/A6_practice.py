class ReverseWord:

    def reverseWords(self, s: str) -> str:
        return " ".join(list(reversed(s.strip().split())))

if __name__ == "__main__":
    s = "the sky is blue"
    # Expected Output: "blue is sky the"
    print(ReverseWord().reverseWords(s=s))
    