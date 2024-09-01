import os
import sys
sys.path.append('/home/vin/DSA')

def count_lines_of_code(directory):
    total_lines = 0
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.py'):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    total_lines += len(lines)
                    print(f"{filename}: {len(lines)} lines")
    print(f"\nTotal lines of code: {total_lines}")

if __name__ == "__main__":
    directory = "/home/vin/DSA"
    count_lines_of_code(directory)


"""
Interview_lti.py: 82 lines
count_lines.py: 19 lines
Interview_hackerrank.py: 123 lines
duplicates.py: 50 lines
test.py: 0 lines
1_fibonacci_sequence_top_down.py: 40 lines
2_fibonacci_sequence_bottom_down.py: 14 lines
classes.py: 22 lines
pointers.py: 35 lines
5_get.py: 101 lines
2_pop.py: 58 lines
6_set.py: 110 lines
constructor.py: 25 lines
7_insert.py: 117 lines
8_remove.py: 131 lines
4_pop_first.py: 72 lines
1_append.py: 40 lines
3_prepend.py: 68 lines
swap_first_and_last.py: 80 lines
reverse.py: 79 lines
28_index_of_first_occurance_string.py: 11 lines
3190_divisible_by_three.py: 32 lines
1_remove_element.py: 55 lines
2_max_min.py: 18 lines
3_longest_string.py: 19 lines
4_remove_duplicates.py: 41 lines
5_max_profit.py: 53 lines
1_merge_sort.py: 23 lines
1_quick_sort.py: 30 lines
2_push.py: 36 lines
1_stack_constructor.py: 23 lines
5_enqueue.py: 39 lines
6_dequeue.py: 55 lines
3_pop.py: 51 lines
4_queue_constructor.py: 23 lines
O2n-drop_constants.py: 22 lines
O1.py: 9 lines
On2.py: 14 lines
On.py: 11 lines
drop_non_dominants.py: 26 lines
nlogn.py: 2 lines
4_dfs_in_order.py: 34 lines
3_dfs_post_order.py: 34 lines
1_bfs.py: 37 lines
2_dfs_pre_order.py: 32 lines
II_kth_smallest_node.py: 71 lines
I_validate_bst.py: 72 lines
A2_longest_common_preix.py: 22 lines
A2_remove_element.py: 18 lines
A1_merge_sorted_array.py: 19 lines
test_merge_sorted_array.py: 17 lines
1_add_vertex.py: 19 lines
2_add_edge.py: 30 lines
4_remove_vertex.py: 82 lines
3_remove_edge.py: 67 lines
2_remove.py: 59 lines
1_insert.py: 51 lines
constructor.py: 17 lines
3_Sink_Down.py: 91 lines
Interview_Maximum_Element_in_a_Stream.py: 119 lines
interview_kth_smallest.py: 87 lines
test.py: 0 lines
E1_difference_of_two_arrays.py: 26 lines
E2_unique_number_of_occurrences.py: 16 lines
C1_practice.py: 28 lines
A3_practice.py: 15 lines
B3_practice.py: 25 lines
E1_practice.py: 27 lines
A1_practice.py: 14 lines
B2_practice.py: 15 lines
A2_practice.py: 23 lines
AM1_practice.py: 20 lines
A6_practice.py: 10 lines
E2_practice.py: 16 lines
B1_practice.py: 18 lines
D1_practice.py: 16 lines
A5_practice.py: 24 lines
B4_practice.py: 21 lines
D2_practice.py: 24 lines
A4_practice.py: 20 lines
D2_pivot_index.py: 20 lines
D1_highest_altitude.py: 17 lines
A2_greatest_common_divisor_of_strings.py: 24 lines
A6_reverse_words_string.py: 23 lines
A3_kids_with_the_greatest_number_of_candies.py: 13 lines
A5_reverse_vowels_of_string.py: 23 lines
M1_product_except_self.py: 0 lines
A4_can_place_flowers.py: 21 lines
M3_string_compression.py: 30 lines
M2_increasing_triplet_sequence.py: 20 lines
A1_merge_strings_alternately.py: 14 lines
B1_move_zeros.py: 10 lines
B2_is_subsequence.py: 11 lines
M2_max_number_of_two_sum_pairs.py: 27 lines
M1_container_with_most_water.py: 21 lines
B2_max_number_two_sum_pair.py: 24 lines
C2.py: 21 lines
C1_maximum_average_subarray_I.py: 25 lines
test_merge_strings.py: 27 lines
test_kids_with_the_greatest_number_of_candies.py: 17 lines
test_greatest_common_divisor_of_strings.py: 44 lines
2_insert.py: 99 lines
3_minimum_value.py: 101 lines
1_contains.py: 81 lines
1_insert.py: 33 lines
2_contains.py: 59 lines
constructor_bst.py: 13 lines
2_selection_sort.py: 13 lines
3_insertion_sort.py: 11 lines
1_bubble_sort.py: 10 lines
bubble_sort_of_ll.py: 83 lines
constructor.py: 18 lines
1_set.py: 28 lines
3_keys.py: 47 lines
2_get.py: 37 lines
interview.py: 269 lines
5_get.py: 93 lines
2_pop.py: 56 lines
constructor.py: 31 lines
7_insert.py: 111 lines
8_remove.py: 128 lines
6_set_value.py: 107 lines
4_pop_first.py: 81 lines
ll_under_the_hood.py: 20 lines
1_append.py: 35 lines
print_list.py: 15 lines
9_reverse.py: 143 lines
3_prepend.py: 64 lines
kth_node.py: 61 lines
middle_node.py: 46 lines
4_partition_list.py: 216 lines
has_loop.py: 57 lines
duplicates_2.py: 142 lines
binary_to_decimal.py: 58 lines
A1_closest_number_to_zero.py: 24 lines
A2_merge_strings_alternatively.py: 11 lines
A3_is_subsequence.py: 16 lines

Total lines of code: 6044
"""