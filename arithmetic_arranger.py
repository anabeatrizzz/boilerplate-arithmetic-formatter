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
		# Colocando maior len entre o primeiro e segundo operador
		maxLen.append(max(lenSegundo, lenPrimeiro))
		
	if mostrar:
		resposta = [eval(r) for r in problems]
		
		# Primeiro numero
		for i, m in enumerate(maxLen):
			texto += f'{primeiro[i].rjust(m + 2)}    '
		texto += "\n"
		# Operador e segundo numero
		for i, m in enumerate(maxLen):
			texto += f'{operador[i]} {segundo[i].rjust(m)}    '
		texto += "\n"
		# Hifens
		for m in maxLen:
			texto += f'{"-" * (m + 2)}    '
		texto += "\n"
		# Resposta
		for i, m in enumerate(maxLen):
			texto += f'{str(resposta[i]).rjust(m + 2)}    '
		
	else:
		texto = ""
		# Primeiro numero
		for i, m in enumerate(maxLen):
			texto += f'{primeiro[i].rjust(m + 2)}    '
		texto += "\n"
		# Operador e segundo numero
		for i, m in enumerate(maxLen):
			texto += f'{operador[i]} {segundo[i].rjust(m)}    '
		texto += "\n"
		# Hifens
		for m in maxLen:
			texto += f'{"-" * (m + 2)}    '
	
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