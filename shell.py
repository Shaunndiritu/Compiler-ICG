import basic

while True:
	text = input('basic > ')
	if text.strip() == "":
		continue

	ast, error, tokens, tac_instructions = basic.run('<stdin>', text, show_tokens=True, show_tac=True)

	if error:
		print(error.as_string())
	else:
		print("Tokens: ")
		for token in tokens:
			print(token)
		print("\nParse Tree: ")
		print(ast)

		print("\nThree-Address Code (ICG): ")
		for instr in tac_instructions:
			print(instr)
