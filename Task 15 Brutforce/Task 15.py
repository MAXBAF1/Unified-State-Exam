for a in range(10000):
	ok = True
	for x in range(1000):
		for y in range(1000):
			if ( (2*x + 3*y < 30) or (x + y >= a) ) == 0:
				ok = False
				break
	if ok == True: print(a)