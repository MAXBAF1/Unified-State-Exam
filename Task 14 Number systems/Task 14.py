a = (49**7)*(7**20) - 7**8 - 28
cnt = 0
while a > 0:
	if a % 7 == 6: cnt += 1
	a //= 7
print(cnt)