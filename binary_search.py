# binary search algorithm

def binary_search(bs_list, searched_element, left, right):
    """Method to search for an element in a list using the binary search algorithm"""
    if right >= left:
        mid = (left + right) // 2
        # we first check if the element we're looking for is in the middle of our list
        if bs_list[mid] == searched_element:
            return searched_element
        # if not, we compare it with the element in the middle; if higher, we search again in the left side of the list
        elif bs_list[mid] < searched_element:
            return binary_search(bs_list, searched_element, mid+1, right)
        # if lower, we search again in the right side of the list
        elif bs_list[mid] > searched_element:
            return binary_search(bs_list, searched_element, left, mid-1)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 1
print(binary_search(list, element, 0, len(list) - 1))
