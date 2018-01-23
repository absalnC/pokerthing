from fractions import Fraction
import math
class Calculator:
	#odd se usa como fracc,pero no es igual,tener cuidado
	def oddToProb(self,odd):
		num,den=odd
		return float(num)/(num+den)

	def probToOdd(self,prob):
		if prob==1:
			return(1,0)
		fracc=Fraction(prob)
		haps=fracc.numerator
		nothaps=fracc.denominator-fracc.numerator
		while(haps>1000):
			haps/=10
			nothaps/=10
		haps=math.floor(haps)
		nothaps=math.floor(nothaps)
		fracc=Fraction(haps,nothaps)
		haps=fracc.numerator
		nothaps=fracc.denominator
		return (haps,nothaps)
	#se considera el pot antes de apuesta 
	def betToPot(self,bet,pot):
		return float(bet)/(pot+bet)
	
	#def expectedValue(self,bet,pot,prob=None,odd=None):

	def isProfitable(self,bet,pot,prob=None,odd=None):
		btp=self.betToPot(bet,pot)
		#print("btp:",btp)
		if prob is not None:
			#print("probability:",prob)			
			return prob>btp
		if odd is not None:
			probfromodd=self.oddToProb(odd)
			return probfromodd>btp
	
