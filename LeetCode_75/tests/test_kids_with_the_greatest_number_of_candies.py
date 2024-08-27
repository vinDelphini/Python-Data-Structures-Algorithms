import sys
sys.path.append('/home/vin/DSA/LeetCode_75/1_Array_String_9')

import pytest
from A3_kids_with_the_greatest_number_of_candies import KidsCandies


class TestKidsCandies:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.ms = KidsCandies()

    def test_candies_list_is_empty(self):
        result = self.ms.kidsWithCandies([], 1)
        assert result == []
        