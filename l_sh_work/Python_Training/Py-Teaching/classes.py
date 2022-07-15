
class A(object):
	
	def __init__(self, pole):
		self.__pole = pole
	
	@property
	def pole(self):
		return self.__pole
	
	@pole.setter
	def pole(self, value):
		self.__pole = value

	@pole.deleter
	def pole(self):
		del self.__pole

class B(A):
	
	def __init__(self, pole):
		super(B if type(pole) == str else '', self).__init__(pole)
	
	def display(self):
		print(self.pole)

def main():
	my = B('stroka')
	my.display()
	my.pole = 'my string'
	my.display()

if __name__ == '__main__':
	main()
