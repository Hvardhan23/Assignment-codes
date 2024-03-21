# sum of consecutive numbers Sn= n(n+1)/2 => 2*Sn=n(n+1)
def countConsecutive(N):
	count = 0
	L = 1
	while( L * (L + 1) < 2 * N):
		a = (1.0 * N - (L * (L + 1) ) / 2) / (L + 1)
		if (a - int(a) == 0.0): # a must be integer 
			count += 1
		L += 1
	return count

N = 15
print (countConsecutive(N))
N = 5
print (countConsecutive(N))

