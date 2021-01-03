def arithmetic_arranger(problems, mostrar=False):
	lista = [x.split() for x in problems]
	primeiro = [p[0] for p in lista]
	operador = [o[1] for o in lista]
	segundo = [s[2] for s in lista]
	
	if mostrar:
		resposta = [eval(r) for r in problems]
		# Primeiro numero
		for p in primeiro:
			print(p.rjust(5), "    ", end=" ")
		print()
		# Operador e segundo numero
		for os in range(len(operador)):
			print(operador[os], segundo[os].rjust(3), "    ", end=" ")
		print()
		# Hifens
		for s in range(len(segundo)):
			print("-" * 5, "    ", end=" ")
		print()
		# Resposta
		for r in resposta:
			print(str(r).rjust(5), "    ", end=" ")
		print()
	else:
		# Primeiro numero
		for p in primeiro:
			print(p.rjust(5), "    ", end=" ")
		print()
		# Operador e segundo numero
		for os in range(len(operador)):
			print(operador[os], segundo[os].rjust(3), "    ", end=" ")
		print()
		# Hifens
		for s in range(len(segundo)):
			print("-" * 5, "    ", end=" ")
		print()

	# Erros
	if len(problems) > 5:
		return("Error: Too many problems.")

	for c in primeiro + segundo:
		if not c.isnumeric():
			return("Error: Numbers must only contain digits.")
		elif len(c) > 4:
			return("Error: Numbers cannot be more than four digits.")

	for c in problems:
		if not("+" not in c or "-" not in c):
			return("Error: Operator must be '+' or '-'.")
	
arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])