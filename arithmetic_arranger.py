def arithmetic_arranger(problems, mostrar=False):
	lista = [x.split() for x in problems]
	primeiro = [p[0] for p in lista]
	operador = [o[1] for o in lista]
	segundo = [s[2] for s in lista]
	maxLen = []
	
	for c in range(len(segundo)):
		lenSegundo = len(segundo[c])
		lenPrimeiro = len(primeiro[c])
		maxLen.append(max(lenSegundo, lenPrimeiro))
		
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
		for m in maxLen:
			if m == 1:
				print("-" * (m + 4), "    ", end=" ")
			elif m == 2:
				print("-" * (m + 3), "    ", end=" ")
			elif m == 3:
				print("-" * (m + 2), "    ", end=" ")
			elif m == 4:
				print("-" * (m + 1), "    ", end=" ")
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
		for m in maxLen:
			if m == 1:
				print("-" * (m + 4), "    ", end=" ")
			elif m == 2:
				print("-" * (m + 3), "    ", end=" ")
			elif m == 3:
				print("-" * (m + 2), "    ", end=" ")
			elif m == 4:
				print("-" * (m + 1), "    ", end=" ")
		print()

	# Erros
	if len(problems) > 5:
		return("Error: Too many problems.")

	for c in primeiro + segundo:
		if len(c) > 4:
			return("Error: Numbers cannot be more than four digits.")
		try:
			int(c)
		except:
			return("Error: Numbers must only contain digits.")
		finally:
			pass

	for c in problems:
		if ("/" or "*" or "**") in c:
			return("Error: Operator must be '+' or '-'.")
	
arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])