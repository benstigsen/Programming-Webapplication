class Language:
	def __init__(self, data):
		self.name = data["languageName"]
		
		self.variable = {
			"prefix": data["variablePrefix"],
			"assign": data["variableAssign"]
		}
		
		self.operator = {
			"add": data["operatorAdd"],
			"sub": data["operatorSubtract"],
			"mul": data["operatorMultiply"],
			"div": data["operatorDivide"],
			"mod": data["operatorModulo"]
		}

		self.print = {
			"open": data["printOpen"],
			"close": data["printClose"]
		}
