class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def overlap(l1, r1, l2, r2):
	
	# when area 0, no overlap
	if l1.x == r1.x or l1.y == r1.y or r2.x == l2.x or l2.y == r2.y:
		return False
	# side by side of other
	if l1.x > r2.x or l2.x > r1.x:
		return False
	# when overlapping
	if r1.y > l2.y or r2.y > l1.y:
		return False

	return True

if __name__ == "__main__":
	l1 = Point(0, 5)
	r1 = Point(5, 0)
	l2 = Point(5, 5)
	r2 = Point(10, 0)

	if(overlap(l1, r1, l2, r2)):
		print("Rectangles Overlap")
	else:
		print("Rectangles Don't Overlap")

if __name__ == "__main__":
	l1 = Point(0, 2)
	r1 = Point(2, 5)
	l2 = Point(0, -5)
	r2 = Point(10, -5)

	if(overlap(l1, r1, l2, r2)):
		print("given rectangles overlap")
	else:
		print("given rectangles do not overlap")	