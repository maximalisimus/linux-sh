#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def clear_name(docname,
				slash_replace='-',  # слэш: заменять на минус; используется в идентификаторах документов: типа № 1/2
				quote_replace='',  # кавычки: замены нет - удаляем
				multispaces_replace='\x20', # множественные пробелы на один пробел
				quotes="""“”«»'\""""  # какие кавычки будут удаляться
				):
	docname = re.sub(r'[' + quotes + ']', quote_replace, docname)
	docname = re.sub(r'[/]', slash_replace, docname)
	docname = re.sub(r'[|*?<>:\\\n\r\t\v]', '', docname)  # запрещенные символы в windows
	docname = re.sub(r'\s{2,}', multispaces_replace, docname)
	docname = docname.strip()
	docname = docname.rstrip('-') # на всякий случай
	docname = docname.rstrip('.') # точка в конце не разрешена в windows
	docname = docname.strip()    # не разрешен пробел в конце в windows
	return docname

def slugify(value):
	"""
	Normalizes string, converts to lowercase, removes non-alpha characters,
	and converts spaces to hyphens.
	"""
	import unicodedata
	value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
	value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
	value = unicode(re.sub('[-\s]+', '-', value))

def main():
	'''
	import re
	t = re.compile("[a-zA-Z0-9.,_-]")
	unsafe = "abc∂éåß®∆˚˙©¬ñ√ƒµ©∆∫ø"
	safe = [ch for ch in unsafe if t.match(ch)]
	# => 'abc'
	'''
	'''
	s = "Hello$@ Python3&_"
	import re
	s1 = re.sub("[^A-Za-z0-9]", "", s)
	print(s1)
	# Результат: HelloPython3
	'''

if __name__ == '__main__':
	main()
