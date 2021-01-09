def arithmetic_arranger(problems, mostrar=False):
	texto = ""
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
			texto += f'{p.rjust(5)}    '
		texto += "\n"
		# Operador e segundo numero
		for os in range(len(operador)):
			texto += f'{operador[os]} {segundo[os].rjust(3)}    '
		texto += "\n"
		# Hifens
		for m in maxLen:
			if m == 1:
				texto += f'{"-" * (m + 4)}    '
			elif m == 2:
				texto += f'{"-" * (m + 3)}    '
			elif m == 3:
				texto += f'{"-" * (m + 2)}    '
			elif m == 4:
				texto += f'{"-" * (m + 1)}    '
		texto += "\n"
		# Resposta
		for r in resposta:
			texto += f'{str(r).rjust(5)}    '
		
	else:
		texto = ""
		# Primeiro numero
		for p in primeiro:
			texto += f'{p.rjust(5)}    '
		texto += "\n"
		# Operador e segundo numero
		for os in range(len(operador)):
			texto += f'{operador[os]} {segundo[os].rjust(3)}    '
		texto += "\n"
		# Hifens
		for m in maxLen:
			if m == 1:
				texto += f'{"-" * (m + 4)}    '
			elif m == 2:
				texto += f'{"-" * (m + 3)}    '
			elif m == 3:
				texto += f'{"-" * (m + 2)}    '
			elif m == 4:
				texto += f'{"-" * (m + 1)}    '
		texto += "\n"
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
	return texto
	
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))