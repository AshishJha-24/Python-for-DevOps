my_set= {1,2,3,4,5}
print(my_set)


my_set.add(6) # adding an element
print("adding 6 ", my_set)

my_set.remove(3) # Removing an element
print("3 is removed ",my_set)

# Set Operationns 

set1 = {1,2,3,4,5,6}
set2 = {4,5,6}

union_set=  set1.union(set2)  # union of sets
print("Union of sets : ",union_set)
InterSectionOfSet = set1.intersection(set2) # Intersection of sets 
print("Intersetion of sets ", InterSectionOfSet)


Difference_set = set1.difference(set2)  # difference of sets
print("Differences in sets ",Difference_set)

is_subset = set1.issubset(set2)  # Checking if set1 is a subset of set2
print("set1 is subset of set2 ",is_subset)

is_superset=set1.issuperset(set2) #Checking if set1 is a superset of set2

print("is set1 is superset of set2",is_superset)


