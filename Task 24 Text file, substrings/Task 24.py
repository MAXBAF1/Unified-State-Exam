f = open('24.txt')
l = f.readline().replace('XZZY', ' ').split()
mx = max(l, key = len)
print(len(mx)+6, mx)