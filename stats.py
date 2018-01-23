from itertools import combinations
import deck
class Stats:
	'''
		La idea de esta clase es poder construir rangos con ella,visualizarlos y poder obtener 
		subconjuntos de
		los mismos rapidamente para calcular equity, fold equity y odds implicitas con agilidad.		
	'''
	d=deck.Deck()
	allcomb=list(combinations(d.cards,2))
	pairs=[]
	highs=[]
	suitedConn=[]
	offsuitedConn=[]
	prange=[]
	def getPairs(self):
		res=[]
		cp=list(self.allcomb)
		for x in cp:
			one,two=x
			c1,v1=one
			c2,v2=two
			if v1==v2:
				res.append(tuple(x))
		return res
	def getPremium(self):
		highpairs=[1,12,13]
		others=[12,13]
	def getPairPlus(num):
		pass
	def petCouplePlus(couple):
		pass
	def getSuitedConnPus(num):
		pass
	def getOffConnPlus(num):
		pass	
	def filterWithColors(one=None,two=None):
		pass
	def filterWithNumbersPlus(one=None,two=None):
		pass
	def buildRange(perc):
		pass		
	def removeRange():
		pass
	def subsetRange():
		pass