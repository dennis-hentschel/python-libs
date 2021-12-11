def invertColour(c):
	if type(c) == str:
		hex = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
		r = ""
		for l in c:
			r += hex[15 - hex.index(l)]
		return r
	elif type(c) == tuple:
		rgb = [0,0,0]
		rgb[0],rgb[1],rgb[2] = c
		for i in range(3):
			rgb[i] = 255 - rgb[i]
		return tuple(rgb)
	return -1

def convertColour(c):
	hex = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
	if type(c) == str:
		first=0
		second=0
		third=0
		mode=False
		digit=0
		for l in c:
			if mode == False:
				toWrite = hex.index(l) * 16
				if digit == 0: first = toWrite
				elif digit == 2: second = toWrite
				elif digit == 4: third = toWrite
			elif mode == True:
				toAdd = hex.index(l)
				if digit == 1: first += toAdd
				elif digit == 3: second += toAdd
				elif digit == 5: third += toAdd
			mode = not mode
			digit += 1
		return (first, second, third)
	if type(c) == tuple:
		return
	return
