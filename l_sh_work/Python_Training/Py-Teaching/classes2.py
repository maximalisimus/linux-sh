#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class TubeStr:

	@classmethod
	def verify_str(cls, value):
		if type(value) != str:
			raise TypeError('Enter the line!')

	def __set_name__(self, owner, name):
		self.name = "__" + name

	def __get__(self, instance, owner):
		return getattr(instance, self.name)

	def __set__(self, instance, value: str):
		self.verify_str(value)
		setattr(instance, self.name, value)

class TubeBool:

	@classmethod
	def verify_bool(cls, value):
		if type(value) != bool:
			raise TypeError('Enter the boolean!')

	def __set_name__(self, owner, name):
		self.name = "__" + name

	def __get__(self, instance, owner):
		return getattr(instance, self.name)

	def __set__(self, instance, value: bool):
		self.verify_bool(value)
		setattr(instance, self.name, value)

class A(object):

	pole1 = TubeStr()
	pole2 = TubeBool()

	def __init__(self, **kwargs):
		self.pole1 = kwargs.get('pole1', '')
		self.pole2 = kwargs.get('pole2', False)

class B(A):

	def __init__(self, **kwargs):
		super(B, self).__init__(**kwargs)

	def display(self):
		print(self.pole1, self.pole2)

def main():
	my1 = A()
	print(my1.__dict__)
	my2 = B(pole1 = 'Stroka - 1', pole2 = True)
	print(my2.__dict__)
	my2.pole1 = str(False)
	print(my2.__dict__)

if __name__ == '__main__':
	main()
