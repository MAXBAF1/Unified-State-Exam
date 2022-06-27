f = open('17.txt')
l = [int(i) for i in f]
k = [i for i in l if i % 2 == 0]
sr = sum(k)/len(k)
mx = cnt = 0
for i in range(len(l)-1):
	if (l[i] % 3 == 0 or l[i+1] % 3 == 0) and (l[i] < sr or l[i+1] < sr):
		cnt += 1
		mx = max(mx, l[i] + l[i+1])
print(cnt, mx)