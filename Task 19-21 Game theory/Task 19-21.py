from functools import lru_cache
@lru_cache(None)
def f(x):
	if x >= 165: return 0
	moves = [f(x+1), f(x*2)]
	lose = [i for i in moves if i <= 0]
	if lose: res = -max(lose) + 1
	else: res = -max(moves)
	return res

for s in range(1, 165):
	print(s, f(s))