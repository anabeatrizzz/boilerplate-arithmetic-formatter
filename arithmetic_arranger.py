def arithmetic_arranger(problems, mostrar=False):
	lista = [x.split() for x in problems]
	primeiro = [p[0] for p in lista]
	segundo = [s[2] for s in lista]
	resposta = [eval(r) for r in problems]

	for i, v in enumerate(lista):
		print(
			v[0].rjust(2*3), "\n",
			v[1], v[2].rjust(3), "\n", "-----".rjust(5), "\n",
			str(resposta[i]).rjust(5), "\n"
		)
	
	# Erros
	if len(problems) > 5:
		raise Exception("Error: Too many problems.")

	for c in primeiro + segundo:
		if not c.isnumeric():
			raise Exception("Error: Numbers must only contain digits.")
		elif len(c) > 4:
			raise Exception("Error: Numbers cannot be more than four digits.")

	for c in problems:
		if not("+" not in c or "-" not in c):
			raise Exception("Error: Operator must be '+' or '-'.")
	

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "32 - 698"])