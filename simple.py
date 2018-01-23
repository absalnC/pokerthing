from operator import attrgetter
ranking=["royal","flush","poker","full","straight","three","pair","single"]
colors=["diamonds","hearts",""]
stack={"small":(0,40),"medium":(41,80),"deep":(80,200)}
def effectiveStack(players):
	return max(players,key=attrgetter('stack'))
