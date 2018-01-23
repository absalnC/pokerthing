class Player:
	stack = 0
	cards={}
	bankroll=0
	history=[]
	def howMany(self,buyin):
		return self.bankroll/buyin
	def howMuch(self,somany,buyin):
		return buyin*somany
	def bet(self):
		return 0
	def raiseup(self):
		return 0
	def fold(self):
		return 0
	def allin(self):
		return 0