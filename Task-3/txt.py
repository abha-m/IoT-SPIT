<<<<<<< HEAD
with open('f.txt') as f:
	polyShape = []
	for line in f:
		line = line.split() # to deal with blank 
		if line:            # lines (ie skip them)
			line = str([int(i) for i in line])
			line=line[1:len(line)-1]
			polyShape.append(line)
for i in polyShape:
    str1 = ''.join(str(i))
=======
with open('f.txt') as f:
	polyShape = []
	for line in f:
		line = line.split() # to deal with blank 
		if line:            # lines (ie skip them)
			line = str([int(i) for i in line])
			line=line[1:len(line)-1]
			polyShape.append(line)
for i in polyShape:
    str1 = ''.join(str(i))
>>>>>>> 6955c080d9a647ce01af530b8fbe5147aa14ca6b
    print (str1)