
class A(object):
	
	def __init__(self, pole):
		self.__pole = pole
	
	@property
	def pole(self):
		return self.__pole
	
	@pole.setter
	def pole(self, value):
		if type(value) == str:
			self.__pole = value
		else:
			raise TypeError('Не верный тип данных! Введите строчный тип данных!')

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
	my.pole = '123'
	my.display()

if __name__ == '__main__':
	main()
