# merge sort algorithm - divide and conquer

def merge_sort(ms_list):
    """Method to break the list in small parts of maximum 1 element"""
    length = len(ms_list)
    if length == 1:
        return ms_list  # list is already sorted
    middle = length // 2
    left_partition = merge_sort(ms_list[:middle])
    right_partition = merge_sort(ms_list[middle:])
    return merge_list(left_partition, right_partition)


def merge_list(left, right):
    """Method to sort the list and merge it back together"""
    # creating an empty list to which we'll add the sorted elements
    sorted_list = []
    i = j = 0  # pointers used to iterate through both lists

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


unsorted_list = [25, 4, 3, -1, 0, 20, 2, 8, 9]
print(merge_sort(unsorted_list))
