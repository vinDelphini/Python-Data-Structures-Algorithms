import sys
sys.path.append('/home/vin/DSA/LeetCode_75/1_Array_String_9')

import pytest
from A1_merge_strings_alternately import MergeStrings

class TestMergeStrings:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.ms = MergeStrings()

    def test_merge_equal_length(self):
        result = self.ms.mergeAlternately("abc", "def")
        assert result == "adbecf"

    def test_merge_word1_longer(self):
        result = self.ms.mergeAlternately("abcd", "ef")
        assert result == "aebfcd"
    
    def test_merge_word2_longer(self):
        result = self.ms.mergeAlternately("ab", "cdef")
        assert result == "acbdef"
    
    def test_merge_both_empty(self):
        result = self.ms.mergeAlternately("", "")
        assert result == ""
