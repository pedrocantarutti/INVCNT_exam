#! /usr/bin/python3


def aux(lst):
    """ Simple auxiliary function to pick only the counter result. """
    return merge(lst)[1]


def merge(lst):
    """ Core recursive function to sort a list of integers
    values based on the divide and conquer approach.  """
    if len(lst) < 2:
        return lst, 0
    mid_index = int(len(lst) / 2)
    left_side, l_inv_counter = merge(lst[:mid_index])
    right_side, r_inv_counter = merge(lst[mid_index:])
    final_array, f_inv_counter = merge_sort(left_side,
                                                             right_side)
    return final_array, (l_inv_counter + r_inv_counter + f_inv_counter)


def merge_sort(left_side, right_side):
    """ Core function to sort a list of integers
    values based on the divide and conquer approach.  """
    final_array = []
    count = 0
    i, j = 0, 0
    left_len = len(left_side)
    while i < left_len and j < len(right_side):
        if left_side[i] <= right_side[j]:
            final_array.append(left_side[i])
            i += 1
        else:
            final_array.append(right_side[j])
            count += left_len - i
            j += 1
    final_array += left_side[i:]
    final_array += right_side[j:]
    return final_array, count
