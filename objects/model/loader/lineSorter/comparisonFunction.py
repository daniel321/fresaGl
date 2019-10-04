
def cmp(command1, command2):
	""" comparison function """
	if ((command1 == "") or (command1 == "g00") or (command1[0] == 'f') or (command1 == "\n")):
		return -1

	if ((command1 == "") or (command2 == "g00") or (command2[0] == 'f') or (command1 == "\n")):
		return 1

	x1 = (command1[0] == 'x')	
	x2 = (command2[0] == 'x')	

	y1 = (command1[0] == 'y')	
	y2 = (command2[0] == 'y')	

	z1 = (command1[0] == 'z')	
	z2 = (command2[0] == 'z')	

	if((x1 and y2) or (y1 and z2) or (x1 and z2)):
		return -1

	if((x2 and y1) or (y2 and z1) or (x2 and z1)):
		return 1
		
	return 0