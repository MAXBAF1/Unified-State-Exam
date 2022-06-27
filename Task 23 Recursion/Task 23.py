def f(x, fin):
	if x > fin: return 0
	if x == fin: return 1
	if x < fin: return f(x+1, fin) + f(x+2, fin) + f(x*2, fin)
print(f(3,10)*f(10,12))