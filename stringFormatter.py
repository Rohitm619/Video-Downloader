with open('links.txt','r') as file:
	with open('link2.txt','w') as file2:
		lines = file.readlines()
		for i in range(len(lines)):
			line = lines[i].split(" ")[1]
			file2.write(line)
