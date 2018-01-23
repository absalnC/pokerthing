from itertools import combinations
class Wizard:
	
	#calculate game changers of one player against another

	#calculate outs of player against others on a given hand
	#classify a hand given the 5 cards(color,value)
	def classify(five):
		rank="single"
		five.sort(key=lambda k:(-k[1],k[0]))
		fivecol,fivenum=five
		if is_royal(five):
			return "royal"
		#is flush?
		#is poker?
		fours=combinations(fivenum,4)
		for fourth in fours:			
			colors,numbers=fourth
			if numbers[1]==numbers[0] and numbers[1]==numbers[2] and numbers[1]==numbers[4]:
				st1=set(fivenum)
				diff=st1.difference(numbers[0])
				return {"class":"poker","number":numbers[0],"others":diff}
		#is triple?
		#is pair?
		pairs=combinations()
		
	#get best hand given the pair and flop,turn and river cards
	#find combinations of size n with all cards the same(inefficient)
	def findNequal(n,cards,option="number"):
		matches=[]
		ns=combinations(cards,n)
		for nth in ns:			
			colors,numbers=nth
			st=set(numbers)
			if len(st)==1:
				st2=set(numbers)
				diff=st.difference(st2)
				matches.append({"nth":n,"number":numbers[0],"others":diff})
		return matches
	def isRoyal(five):
		if isStraight(five) and isFlush(five) and highest(five)==1:
			return True
		return False
	def isStraight(self,five):
		values=list(v for k,v in five)
		values.sort()
		for x in range(len(values)-1):
			#si no es escalera tipica
			if abs(values[x]-values[x+1])!=1:
				#valores de 10,j,q y k
				check=list(range(10,14))
				#si el as no estra en la mano, o alguno de la escalera al as no esta en mano
				if not 1 in values or not all(v in values for v in check):					
					return False				
		return True

	def isFlush(self,five):
		colors=set(c for c,v in five)
		return len(colors)==1
	def highest(self,five):
		mx=0		
		for c,v in five:
			if v==1:
				return 1
			elif v>mx:
				mx=v
		return mx

