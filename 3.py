
def maxWater(arr, n): 
	res = 0
	for i in range(1, n - 1): 
		left = arr[i] 
		for j in range(i): 
			left = max(left, arr[j]) 
		right = arr[i] 
		for j in range(i + 1, n): 
			right = max(right, arr[j]) 
		res = res + (min(left, right) - arr[i]) 
	return res 

if __name__ == "__main__": 
	arr = [0, 1, 0, 4, 1, 0, 
		3, 2, 2, 6, 5, 1] 
	n = len(arr) 

	print(maxWater(arr, n)) 

