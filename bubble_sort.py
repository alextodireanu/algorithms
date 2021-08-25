# bubble sort algorithm

def bubble_sort(bs_list):
    """Method to bubble sort a given list"""
    n = len(bs_list)
    # reading all the elements in our list
    for i in range(n-1):
        for j in range(n-i-1):
            if bs_list[j] > bs_list[j+1]:
                bs_list[j], bs_list[j+1] = bs_list[j+1], bs_list[j]
    return bs_list


unsorted_list = [1, 4, 6, 2]
print(bubble_sort(unsorted_list))
