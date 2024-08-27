import sys
sys.path.append('/home/vin/DSA/LeetCode_75/1_Array_String_9')

import pytest
from A2_greatest_common_divisor_of_strings import GCDOfStrings


class TestGCDStrings:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.ms = GCDOfStrings()
    
    def test_empty_strings(self):
        result = self.ms.gcdOfStrings("", "")
        assert result == ""
    
    def test_common_divisor(self):
        result = self.ms.gcdOfStrings("ABCABC", "ABC")
        assert result == "ABC"
    
    def test_no_common_divisor(self):
        result = self.ms.gcdOfStrings("DOG", "GOD")
        assert result == ""
 
    def test_one_string_is_repeated_version_of_other(self):
        result = self.ms.gcdOfStrings("ABABABABAB", "AB")
        assert result == "AB"
    
    def test_identical_strings(self):
        result = self.ms.gcdOfStrings("AAAA", "AAAA")
        assert result == "AAAA"
    
    def test_one_empty_string(self):
        result = self.ms.gcdOfStrings("ABABABAB", "")
        assert result == ""
    
    def test_both_strings_empty(self):
        result = self.ms.gcdOfStrings("", "")
        assert result == ""
    
    def test_length_of_first_string_lower(self):
        result = self.ms.gcdOfStrings("ABCDABCD", "ABCDABCDABCDABCDABCD")
        assert result == "ABCD"
