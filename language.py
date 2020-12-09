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
		
		if _data["variablePrefix"] == _data["variableAssign"]:
			_data["variablePrefix"] = "var"
			_data["variableAssign"] = "="

		self.variable = {
			"prefix": _data["variablePrefix"] 	if (len(_data["variablePrefix"]) > 0) else "var",
			"assign": _data["variableAssign"] 	if (len(_data["variableAssign"]) > 0) else "="
		}
		
		self.operator = {
			"add": _data["operatorAdd"] 		if (len(_data["operatorAdd"]) > 0) 		else "+",
			"sub": _data["operatorSubtract"] 	if (len(_data["operatorSubtract"]) > 0) else "-",
			"mul": _data["operatorMultiply"] 	if (len(_data["operatorMultiply"]) > 0) else "*",
			"div": _data["operatorDivide"] 		if (len(_data["operatorDivide"]) > 0) 	else "/",
			"mod": _data["operatorModulo"] 		if (len(_data["operatorModulo"]) > 0) 	else "%"
		}

		self.print = {
			"open": _data["printOpen"] 			if (len(_data["printOpen"]) > 0) 	else "print(",
			"close": _data["printClose"] 		if (len(_data["printClose"]) > 0) 	else ")"
		}

	def generateExample(self):
		return (
			f'{self.variable["prefix"]} message {self.variable["assign"]} "Hello World!"\n'
			f'{self.variable["prefix"]} x {self.variable["assign"]} 5\n'
			f'{self.variable["prefix"]} y {self.variable["assign"]} 7\n'
			f'\n'
			f'{self.print["open"]} message {self.print["close"]}\n'
			f'{self.print["open"]} x {self.operator["add"]} y {self.print["close"]}\n'
		)

class ExampleLanguage(Language):
	def __init__(self):
		data = {
			"languageName": 	"Example Language",

			"variablePrefix": 	"VAR",
			"variableAssign": 	"=",

			"operatorAdd": 		"ADD",
			"operatorSubtract": "SUB",
			"operatorMultiply": "MUL",
			"operatorDivide": 	"DIV",
			"operatorModulo": 	"MOD",

			"printOpen": 		"PRINT(",
			"printClose": 		")"
		}

		super().__init__(data)
