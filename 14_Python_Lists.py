mylist = ["apple", "banana", "cherry"]
print(mylist)
print(type(mylist))
print(len(mylist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


list1 = ["abc", 34, True, 40, "male"]
mynewlist = list(list1)
print(mynewlist)

if 'male' in list1:
    print('the male is in the list')

# Access List Items
print('Access List Items')
print(list1[1])
print(list1[-1])
print(list1[2:4])
print(list1[-4:-1])

#  Change List Items
print('Change List Items')
thislist = ["apple", "banana", "cherry"]
thislist[1] = "pear"
print(thislist)
thislist[1:] = ["nagaraj"]
print(thislist)
thislist.insert(0,'naga')
print(thislist)
thislist.append('raju')
print(thislist)
thislist.extend(list2)
print(thislist)
thislist.extend(tuple(list3))
print(thislist)

# Remove List Items
print('Remove List Items')
thislist.remove('apple')
print(thislist)
thislist.pop()
print(thislist)
thislist.pop(3)
print(thislist)
del thislist[0]
print(thislist)
thislist.clear()
print(thislist)

# Loop Lists
print('Loop Lists')
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
for i in range(len(thislist)):
    print(thislist[i])

i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1
[print(x) for x in thislist]

# List Comprehension
print('List Comprehension')
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if 'a' in x:
        newlist.append(x)
print(newlist)

newlist = [x for x in fruits if 'a' in x]
print(newlist)
newlist = [ x.upper() for x in fruits]
print(newlist)

# Sort Lists
print('Sort Lists')
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist.sort(reverse=True)
print(thislist)

def custfun(n):
    return abs( n - 1 )
lists = [10, 2, 3, 40, 60]
lists.sort(key = custfun)
print(lists)
lists.reverse()
print(lists)

# Copy Lists
print('Copy Lists')
thislist = ["apple", "banana", "cherry"]
copiedlist = thislist
print(id(copiedlist), id(thislist))
newlist = thislist.copy()
print(newlist, id(newlist))
newlist1 = list(newlist)
print(newlist1, id(newlist1))
newlist2 = thislist[:2]
print(newlist2, id(newlist2))

# Join Lists
print('Join Lists')
list1 = ["apple", "banana", "cherry"]
list2 = [10, 20, 30]
list3 = list1 + list2
print(list3)
list1.extend(list2)
print(list1)
for x in list2:
    list1.append(x)
print(list1)
