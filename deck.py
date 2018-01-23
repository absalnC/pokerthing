import random as rand
class Deck:
	cards=[]
	colors=["diamond","heart","spades","clubs"]
	numbers=[x for x in range(1,14)]
	def __init__(self):
		self.cards=[(col,number) for col in self.colors for number in self.numbers ]
	#atencion, devuelve lista con una carta		
	def giveOne(self):
		choice=self.cards[-1:]
		self.cards=self.cards[:-1]
		return choice
	def giveN(self,n):
		choice=self.cards[-n:]
		self.cards=self.cards[:-n]
		return choice
	def shuffle(self):
		self.cards=[(col,number) for col in self.colors for number in self.numbers ]
		rand.shuffle(self.cards)
	def sort(self):
		self.cards.sort(key=lambda k:(k[1],k[0]))
