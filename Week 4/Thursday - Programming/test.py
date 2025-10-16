class Computer(object):
	def __init__(self):
		self.__maxprice = 900  # restrict access/no modification

	def sell(self):
		print("Selling Price: {}".format(self.__maxprice))

	def setMaxPrice(self, price):
		self.__maxprice = price

# Output:
c = Computer()
c.sell()      # prints normal

# change the price (this creates a new attribute, it won't change the "private" one)
c.__maxprice = 1000
c.sell()      # this will still print 900 because of name mangling

# using setter function
c.setMaxPrice(1000)
c.sell()
