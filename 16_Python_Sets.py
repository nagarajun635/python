myset = {"apple", "banana", "cherry"}
print(myset)

myset1 = {"apple", "banana", "cherry", "apple", "banana", "cherry"}
print(myset1)

mylist2 = {1, True, 0, False}
print(len(mylist2))
print(mylist2)
print(len(mylist2))

myset = {"apple", "banana", "cherry"}
print(type(myset))

set1 = set(["apple", "banana", "cherry"])
print(set1)
set2 = set(("apple", "banana", "cherry"))
print(set2)

# Access Items
print('Access Items')
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
print('banana' in thislist)
print('banana' not in thislist)

# Add Items
print('Add Items')
thiset2 = set(["apple", "banana", "cherry"])
print(thiset2)
thiset2.add("orange")
print(thiset2)

thiset2.update(mylist2)
print(thiset2)
thiset2.update(mylist2)
print(thiset2)

# Remove Item
print('Remove Item')
thiset3 = set(["apple", "banana", "cherry"])
thiset3.remove('apple')
print(thiset3)
thiset3.discard('orange')
thiset3.pop()
print(thiset3)
thiset3.clear()
print(thiset3)
del thiset3

# Loop Items
print('Loop Items')
thisset = set(["apple", "banana", "cherry"])
for x in thisset:
    print(x)

# Join Sets
print('Join Sets')
set1 = {'a', 'b', 'c'}
set2 = {'d', 'e', 'f'}
set3 = set1.union(set2)
print(set3)
set4 = set1|set2
print(set4)
set5 = {1,2,3,4,5,6,7,8,9}
set6 = set5.union(set1, set2, set3)
print(set6)
set7 = set1 | set2 | set3
print(set7)
set8 = set1.union(('10', '11', '12'))
print(set8)

set1 = {'a', 'b', 'c'}
set2 = {1,2,3}
set1.update(set2)
print(set1)

set1 = {'a', 'b', 'c'}
set2 = {'d', 'e', 'a'}
print(set1.intersection(set2))
print(set1 & set2)
print(set1)
set1.intersection_update(set2)
print(set1, set2)
set1 = {'a', 'b', 'c'}
set2 = {'d', 'e', 'a'}
set4 = set1.difference(set2)
print(set4)
set1.difference_update(set2)
print(set1)
print(set1-set2)

set1 = {'apple', 'banana', 'cherry'}
set2 = {'apple', 'grapes', 'mango'}
set3 = set1.symmetric_difference(set2)
print(set3)
print(set1^set2)
set4 = set1.symmetric_difference_update(set2)
print(set1)

# frozenset
print('frozenset')
fzset = frozenset(['apple', 'banana', 'cherry'])
print(fzset, id(fzset))
fzsetcp = fzset.copy()
print(fzsetcp, id(fzsetcp))

set2 = {1,2,3,4,5,6,7,8,9}
set1 = {4,5,6,7,8,9}
print(set1.issubset(set2))
set1 = {1,2,3,4,5,6,7,8,9}
set2 = {4,5,6,7,8,9,10}
print(set1.issuperset(set2))

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

