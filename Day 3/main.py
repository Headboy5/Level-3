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