"""Write a function called chop that takes a list and modifies it, removing
the first and last elements, and returns None. Then write a function called middle
that takes a list and returns a new list that contains all but the first and last
elements"""


def chop(lst):
    del lst[0]  # This is to remove the first element in list
    del lst[-1]  # This is to remove the last element in the list


def middle(lst):

    new = lst[1:]  # Stores all but the first element
    del new[-1]  # Deletes the last element
    return new


list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]

chop_list = chop(list1)
print(list1)  # Output should be [2,3]
print(chop_list)  # Output should be None

middle_list = middle(list2)
print(list2)  # The list should be unchanged
print(middle_list)  # Output should be [2,3]
