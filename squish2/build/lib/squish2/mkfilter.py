
def mkfilter(filtstr,filtfile):

	f = open(filtfile,'r')	
	items = []
	for line in f:
	        zoo = Dict()
	        zoo[filtstr] = line.rstrip()
	        l = Dict()
	        l.match_phrase = zoo
	        items.append(l)
	
	
	w = Dict()
	w.bool.should = items
	w.bool.minimum_should_match = 1
	return(w.to_dict())


from addict import Dict
