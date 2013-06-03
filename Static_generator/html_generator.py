#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# Author: L. Loewert for GovHack 2013 contest


fread_template = open("template.html", "r")
fread_LGA = open("LGA_names.csv", "r")

content = fread_template.read()


for line in fread_LGA:
		table = line.split(";")
		LGA_number = table[0]
		LGA_name = table[1][:-1]
		fwrite = open("LGA/" + LGA_number + ".html", "w")
		fwrite.write(content.replace("%%LGA_NAME%%",LGA_name))
		fwrite.close
		
