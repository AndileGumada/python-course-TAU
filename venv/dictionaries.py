# dictionaries are type of Python data collection that stores data in key/value pairs
# mutable : can be changed, maintain order as of python 3.7
stuff = {"food": 15 , "energy":100,"enemies":5}

# get() returns the value at a specified key
print(stuff.get("food"))
#
print(stuff.items())
# keys() returns a list containing directory's keys
print(stuff.keys())
print(stuff.popitem())

new_items = {"rocks":4,"stones":6,"arrows":8,"bow":22}
stuff.update(new_items)
print(stuff)
