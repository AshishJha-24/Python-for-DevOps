my_tuple = (1, 2, 'apple', 'banana')
print(my_tuple)

first_element = my_tuple[0]  # Access the first element (1)
print(first_element)

tuple_length = len(my_tuple)  # Length of the tuple (4)
print("Tuple Length : ", tuple_length)

coordinates = (3, 4)
x, y = coordinates  # Unpack the tuple into x and y (x=3, y=4)
print("coordinates are : ",x,y)


new_tuple = my_tuple + (3.14, 'cherry')  # Concatenates my_tuple with a new tuple
print(new_tuple)

is_present = 'apple' in my_tuple  # Checks if 'apple' is in the tuple (True)
print("apple is present in tuple", is_present)
def get_coordinates():
    return (3, 4)

x, y = get_coordinates()  # Unpack the returned tuple (x=3, y=4)

print("coordinates return from function",x,y)

