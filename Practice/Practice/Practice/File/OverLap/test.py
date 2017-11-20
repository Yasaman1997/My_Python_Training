def filetolistofints(filename):
	list_to_return = []
	with open(filename) as f:
		line = f.readline()
		while line:
			list_to_return.append(int(line))
			line = f.readline()
	return list_to_return

primeslist = filetolistofints('primenumbers.txt')
happieslist = filetolistofints('happynumbers.txt')

overlaplist = [elem for elem in primeslist if elem in happieslist]
print(overlaplist)