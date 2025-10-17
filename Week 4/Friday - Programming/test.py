class Circle(object):
	def __init__(self, size, area):
		self.size = size
		self.area = area

	def __add__(self, other):
		return(self.size + other.size, self.area + other.area)

C1 = Circle(4, 50)            # replace small with integer
C2 = Circle(10, 200)          # replace large with integer

print("addition of 2 areas", C1 + C2)
