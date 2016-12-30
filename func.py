#! /usr/bin/python3
#coding=utf-8

def display():
	a = 'hello world!'
	print (a)


display()

def fahrenheit_converter(c):
	fahrenheit = c * 9 / 5 + 32
	return fahrenheit
	
str1 = str(fahrenheit_converter(5)) + 'F'

print(str1)
	


