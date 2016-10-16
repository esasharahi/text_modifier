#!/usr/bin/python
## esasharahi@gmail.com
import re
import os.path
def main():
	input_file = input("Text file address: ")
	with open(input_file) as f:
		file_for_modify = f.read()
		modified_file = open("modified_" + os.path.basename(input_file), 'w')
		for x in "([{":
			bad_regex = r" *" + re.escape(x) + r" *"
			p = re.compile(bad_regex)
			m = p.sub(r" " + x , file_for_modify)
			file_for_modify = m
			
		for x in ")]}":
			bad_regex = r" *" + re.escape(x) + r" *"
			p = re.compile(bad_regex)
			m = p.sub(x + r" " , file_for_modify)
			file_for_modify = m
			
		for x in ",.:;?!،؛":
			bad_regex = r" *" + re.escape(x) + r" *"
			p = re.compile(bad_regex)
			m = p.sub(x + r" " , file_for_modify)
			file_for_modify = m
		modified_file.write(m)
main()
