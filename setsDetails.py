# Sets
# fruits = {"apple", "banana", "cherry"}
# immutable
# print(id(fruits))
# fruits.add("orange")
# print(id(fruits))

#  Duplicates are not allowed
# fruits = {"apple", "banana", "cherry", "apple"}
# print(fruits)


#  Add and Remove Items
"""
fruits = {"apple", "banana", "cherry"}
fruits.remove("apple")
fruits.add("Mango")
print(fruits)
"""

# Updated Set
"""
fruits = {"apple", "banana", "cherry"}
fruits.update(['orange', 'grape'])
print(fruits)
"""


#  Union ( Duplicates are not allowed)
set1 ={1,2,3}
set2 ={2,3, 4,5,6}
result = set1.union(set2)
# print(result)

#  CLear Set
# set1.clear()
# print(set1)

# Intersection
# intersectionResult =set1.intersection(set2)
# print(intersectionResult)

#  Difference
differenceResult = set1.difference(set2)
# print(differenceResult)


# Issubset
set3 = {1,2}
# print(set3.issubset(set1))

#  Issuperset
print(set1.issuperset(set3))





















