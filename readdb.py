def splitLine(db, m):

	txtFile = open(db, "r")
	mag = str(m) + ' '
	for line in txtFile:
		
		if mag in line:
		
			return int(line.strip( ' \n' ).replace(mag, ''))
			
print splitLine("3uztaisas.txt", 1450)