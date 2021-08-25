# linear search algorithm

def linear_search(ls_list, searched_element, length):
    """Method to search for a given element in a list using the linear search algorithm"""
    for i in range(length):
        if ls_list[i] == searched_element:
            return i
    return -1


given_list = [1, 2, 3, 4, 5, 6]
element = 70
print(linear_search(list, element, len(given_list)))
