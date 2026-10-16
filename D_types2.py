print("__________________________________________LIST______________________________________________________")
# list properties
# list is mutable, ordered, allows duplicate elements, and can contain heterogeneous elements.
my_list = [1, 2, 3, 4, 5]
print("The list is:", my_list)

print("The length of the list is:", len(my_list)) # prints the length of the list
my_list.append(29) # add new element to the end of the list
print("The list after appending 29 is:", my_list)
print("___________________________________________SET______________________________________________________")

#set 
#set is mutable, unordered, does not allow duplicate elements, and can contain heterogeneous elements.
set1 = {15,8,3, 26, 5, }
print("The set is:", set1)
set1.add(29) # add new element to the set
print("The set after adding 29 is:", set1)

print("___________________________________________TUPLE______________________________________________________")
#tuple
# tuple is immutable, ordered, allows duplicate elements, and can contain heterogeneous elements.
tuple1 = (1, 6, 2, 9, 5)
print("The tuple is:", tuple1)
# tuple1.append(29) # This will raise an AttributeError since tuples are immutable

print("___________________________________________DICTIONARY______________________________________________________")
#dictionary
# dictionary is mutable, unordered, does not allow duplicate keys, and can contain heterogeneous elements.
dict1 = {"name": ["Onkar","Ayush","Nihal","Kaustubh"], "age": [22,23,24,25], "city": ["Pune ITP"]}
print("The dictionary is:", dict1) # Displays the entire dictionary
