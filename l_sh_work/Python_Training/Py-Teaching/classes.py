
class A(object):
	
	def __init__(self, pole: str = ''):
		self.__pole = pole
	
	@property
	def Pole(self):
		return self.__pole
	
	@Pole.setter
	def Pole(self, value: str):
		self.__pole = value

	@Pole.deleter
	def Pole(self):
		del self.__pole

class B(A):
	
	def __init__(self, pole):
		super(B, self).__init__(pole)
	
	def display(self):
		print(self.Pole)

def main():
	my = B('stroka')
	my.display()
	my.Pole = '123'
	my.display()

if __name__ == '__main__':
	main()
