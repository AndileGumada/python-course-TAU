# list collection of data - can contain any/all data type in a single list
# can contain other collections(list, directories, tuples) as list item
# mutable(items can be added , removed and changed)
# maintain oder(we use index to find item


fruits = ["grapes","peaches","apples","banana","cherries"]
years = [3,"1998",2.5, 987,"1992"]

print(fruits, years)
# append add an object at the end of the list
fruits.append("oranges")
print(fruits)
# extends the list by appending elements at the
fruits.extend(years)
print(fruits)
#
fruits.remove("oranges")
print(fruits)

fruits.pop(0)
# removes an element at a specified position
print(fruits)
# sort() is used to sort lists of like type only
numbers  = [5,231, 18, 78, 2008]
numbers.sort()
print(numbers)
