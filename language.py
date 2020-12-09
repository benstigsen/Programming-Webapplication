i = 0

class Language:
	def __init__(self, data):
		global i
		i += 1

		# Make request form data mutable
		_data = {}
		for key in data:
			_data[key] = data[key].strip()

		# Create easy dictionaries and verify request form data
		self.name = _data["languageName"] 		if (len(_data["languageName"]) > 0) else f"Language {i}"
		
		self.variable = {
			"prefix": _data["variablePrefix"] 	if (len(_data["variablePrefix"]) > 0) else "var",
			"assign": _data["variableAssign"] 	if (len(_data["variableAssign"]) > 0) else "="
		}
		
		self.operator = {
			"add": _data["operatorAdd"] 		if (len(_data["operatorAdd"]) > 0) else "+",
			"sub": _data["operatorSubtract"] 	if (len(_data["operatorSubtract"]) > 0) else "-",
			"mul": _data["operatorMultiply"] 	if (len(_data["operatorMultiply"]) > 0) else "*",
			"div": _data["operatorDivide"] 		if (len(_data["operatorDivide"]) > 0) else "/",
			"mod": _data["operatorModulo"] 		if (len(_data["operatorModulo"]) > 0) else "%"
		}

		self.print = {
			"open": _data["printOpen"] 			if (len(_data["printOpen"]) > 0) else "print(",
			"close": _data["printClose"] 		if (len(_data["printClose"]) > 0) else ")"
		}
