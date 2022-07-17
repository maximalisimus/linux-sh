
class Lines:
	
	@classmethod
	def verify_str(cls, lines):
		if type(lines) != str:
			raise TypeError('Enter the line!')
	
	def __set_name__(self, owner, name):
		self.name = "__" + name
	
	def __get__(self, instance, owner):
		return getattr(instance, self.name)

	def __set__(self, instance, value):
		self.verify_str(value)
		setattr(instance, self.name, value)

class A(object):
	
	pole = Lines()
	
	def __init__(self, pole):
		self.pole = pole

class B(A):
	
	def __init__(self, pole):
		super(B, self).__init__(pole)
	
	def display(self):
		print(self.pole)

def main():
	my1 = A('strings')
	print(my1.pole)
	print(my1.__dict__)
	my2 = B('stroka')
	my2.display()
	my2.pole = '123'
	my2.display()
	print(my2.__dict__)

if __name__ == '__main__':
	main()
