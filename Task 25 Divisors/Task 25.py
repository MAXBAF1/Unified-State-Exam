for i in range(5000, 100000):
	cnt = 0
	for d in range(1, round(i**0.5)+1):
		if i % d == 0:
			if d % 2 != 0: cnt += 1
			if (i//d) % 2 != 0: cnt += 1
			if d == (i//d): cnt -= 1
			if cnt > 5: break
	if cnt == 5: print(i)