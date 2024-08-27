my_list = [1, 2, 3, 'apple', 'banana']
first_element = my_list[0]  # Access the first element (1)
print(first_element)

list_length = len(my_list)  # Length of the list (5)
print("length of the list is ",list_length)

my_list.append(4)  # Adds 4 to the end of the list
print("After appending 4 in the list",my_list)


my_list.remove('apple')  # Removes 'apple' from the list
print("After remove apple from list",my_list)

subset = my_list[1:4]  # Creates a new list with elements at index 1, 2, and 3
print("Subset : ",subset)

new_list = my_list + [5, 6]  # Concatenates my_list with [5, 6]
print(new_list)

my_list.remove("banana")
my_list.sort()  # Sorts the list in ascending order
print(my_list)

is_present = 'banana' in my_list  # Checks if 'banana' is in the list (True)

print("banana is present in list ", is_present)