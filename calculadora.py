#!/usr/bin/python3

import sys


def suma(op1, op2):
	resultado = int(op1) + int(op2)
	return resultado

def resta(op1, op2):
	resultado = int(op1) - int(op2)
	return resultado

def multiplicacion(op1, op2):
	resultado = int(op1) * int(op2)
	return resultado

def division(op1, op2):
	resultado = int(op1)/int(op2)
	return resultado


if __name__ == "__main__":
	args= sys.argv[1:]
	function = args[0]
	operand1 = args[1]
	operand2 = args[2]	
try:
	if function  == "suma":
		resultado = suma(operand1, operand2)
		print(resultado)
	elif function == "resta":
		resultado = resta(operand1, operand2)
		print(resultado)
	elif function  == "multiplicacion":
		resultado = multiplicacion(operand1, operand2)
		print(resultado)
	elif function == "division":
		resultado = division(operand1, operand2)
		print(resultado)
	else:
		print("The function selected does not exist")

except ValueError:
		print("You wrote an incorrect value as an operand")
	
except:
		print("ERROR")

