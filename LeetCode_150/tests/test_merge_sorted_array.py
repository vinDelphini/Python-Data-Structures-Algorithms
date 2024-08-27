import sys
sys.path.append('/home/vin/DSA/LeetCode_150/1_Array_String_24')

import pytest
from A1_merge_sorted_array import MergeSortedArray  #type: ignore


class TestMergeSortedArray:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.ms = MergeSortedArray()

    def test_second_list_is_empty(self):
        result = self.ms.merge([1], 1, [], 0)
        assert result == [1]
        
