
class A(object):
	
	def __init__(self, pole):
		self.__pole = pole
	
	@property
	def Pole(self):
		return self.__pole
	
	@Pole.setter
	def Pole(self, value):
		if type(value) == str:
			self.__pole = value
		else:
			raise TypeError('Не верный тип данных! Введите строчный тип данных!')

	@Pole.deleter
	def Pole(self):
		del self.__pole

class B(A):
	
	def __init__(self, pole):
		super(B if type(pole) == str else '', self).__init__(pole)
	
	def display(self):
		print(self.Pole)

def main():
	my = B('stroka')
	my.display()
	my.Pole = '123'
	my.display()

if __name__ == '__main__':
	main()
