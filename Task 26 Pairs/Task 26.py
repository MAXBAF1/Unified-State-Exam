f = open('26.txt')
n = int(f.readline())
l = [int(i) for i in f]
nechet = [i for i in l if i % 2 != 0]
mx = cnt = 0
for i in range(len(nechet)):
	for j in range(i+1, len(nechet)):
		if nechet[i] % 2 != 0 and nechet[j] % 2 != 0 and (nechet[i]+nechet[j])/2 in l:
			cnt += 1
			mx = max(mx, (nechet[i]+nechet[j])//2)
print(cnt, mx)