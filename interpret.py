output = []

def error(n, msg):
	output.append(f"ERROR LINE [{n + 1}]: {msg}")

def interpret(syntax, content):
	global output
	output = []

	variables = {}

	# Replace math symbols with "proper" math symbols
	content = content.replace(syntax.operator["add"], "+")
	content = content.replace(syntax.operator["sub"], "-")
	content = content.replace(syntax.operator["mul"], "*")
	content = content.replace(syntax.operator["div"], "/")
	content = content.replace(syntax.operator["mod"], "%")
	content = content.replace(syntax.print["open"], f'{syntax.print["open"]} ')
	content = content.replace(syntax.print["close"], f' {syntax.print["close"]}')

	lines = content.split("\n")

	for i, line in enumerate(lines):
		line = line.strip()
		words = line.split(" ")
		
		for word in range(len(words)):
			words[word] = words[word].strip()

		# Get Variables
		if len(words) > 3:
			if words[0] == syntax.variable["prefix"]:
				if words[2] == syntax.variable["assign"]:
					value = line[line.find(f' {syntax.variable["assign"]}') + len(syntax.variable["assign"]) + 1:].strip()

					if value[0] == '"' and value[-1] == '"':
						variables[words[1]] = value[0:]
						continue
					else:
						variables[words[1]] = value 
						continue
				else:
					error(i, f'You did not assign the variable with: {syntax.variable["assign"]}')
					continue

		# Replace Variables
		for j, word in enumerate(words):
			if word in variables:
				words[j] = variables[word]

		# Print
		if words[0] == syntax.print["open"]:
			if words[-1] == syntax.print["close"]:
				text = " ".join(words[1:-1]).strip()

				if len(words) == 2 or len(text) == 0:
					output.append("\n")
					continue

				# Math
				math = False
				for x in range(0, 10):
					if str(x) in text:
						math = True
						try:
							result = eval(text)
							output.append(result)
						except:
							error(i, "Invalid math. Make sure it matches your syntax or that the variables exists")
						break
				if math:
					continue

				# String
				if len(text) >= 2:
					if text[0] == '"' and text[-1] == '"':
						output.append(text[1:-1])
						continue
				
				error(i, 'Unknown variable(s) (put "double quotes" around the text to print directly)')

			else:
				error(i, f'`{syntax.print["open"]}` is not closed with `{syntax.print["close"]}`')
				continue


	return output
	