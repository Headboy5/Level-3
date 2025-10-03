example_string = "Hello, world!"
example_float = 3.14
example_int = 42
example_complex = 2j
example_dict = {"name": "Alice", "age": 25}
example_range = range(6,20)
example_tuple = (1, 2, 3)
example_bool = True
example_list = [1, 2, 3, 4]
example_set = {1, 2, 3}
example_frozenset = frozenset({4, 5, 6})
example_bytes = b"Hello"
example_bytearray = bytearray(5)
example_memoryview = memoryview(bytes(5))
example_none = None

#==ACTIVITY 1==

OrderItem = [1, "Jeff", "Computer", 75.50, True]
print(OrderItem[0], OrderItem[2], OrderItem[4])

# Pick three out of the List Methods (sort, pop, extend, count, copy, clear, reverse) and explain what they do in one or two sentences.
# sort() - This method sorts the elements of a list in ascending order by default. It modifies the original list.
# pop() - This method removes and returns the last item from the list. You can also specify an index to remove an item at a specific position.
# count() - This method returns the number of occurrences of a specified value in the list.

# Give example of how the chosen three lists methods in question 2 can be used in a code.
OrderItem = [1, "Jeff", "Computer", 75.50, True, "Jeff", "Smart"]
sortable = [3, 1, 4, 2]
print(f"Original sortable: {sortable}")
sortable.sort()
print(f"Sorted sortable: {sortable}")
OrderItem.pop()
print(f"OrderItem after pop: {OrderItem}")
print(f"Count of 'Jeff' in OrderItem: {OrderItem.count('Jeff')}")

#==ACTIVITY 2==
avengers = {'JoshBrolin': 'Thanos', 'Robertjunior': 'IronMan', 'Scarlett Johansson':'blackwidow'}
new_avengers = {'Tom Holland': 'Spiderman', 'Chris Hemsworth': 'Thor', 'Chadwick Boseman': 'Black Panther', 'Mark Ruffalo': 'Hulk'}
avengers.update(new_avengers)
print(avengers)

avengers['Scarlett Johansson'] = 'Lucy'
print(avengers)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 'platypus'}
dict1.update(dict2)
print(dict1)

#==ACTIVITY 3==
a1= [1, 2, 3, "a", "b", "c"]
tuplea1 = tuple(a1)
print(type(tuplea1))

# 3. Given these 2 tuples:
game1 = ('tekken7',)
game2 = ('tekken7')
# Explain why the outputs below are different:

print('game1 is of type: ' , type(game1))
print('game2 is of type: ' , type(game2))
# game1 is a tuple because it has a comma after the single element, while game2 is just a string without a comma.

if(input("This code will raise an error, y = run: ") == 'y'):
    numbers = (1, 2, 3)
    numbers[1] = 'x'
    # Explain what happens when you run this code.
    # This code will raise a TypeError because tuples are immutable, meaning their elements cannot be changed after creation.

#==ACTIVITY 4==
a = {1, 2, 3, 4, 5, 6, 7, 8, "banana"}
print(a)

a.add("apple")
print("After add:", a)

a.remove(2)
print("After remove:", a)

a.clear()
print("After clear:", a)

a = {1, 4, 6, 7, 8, 33, 4, "banana", "apple"}
b = {1, 2, 3, 4, 5, 6, 7, 8, "banana"}
diff = a.difference(b)
print("Difference between a and b:", diff)