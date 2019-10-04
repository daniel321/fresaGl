class Splitter(object):

	def divideFile(self,file,start,end):
		lineNum = 0
		lines = file.split('\n')

		begCode  = ""
		midCode = ""
		endCode  = ""

		for line in lines:
			if (line != ""):
				if(lineNum < start):
					begCode += line + "\n"	
				elif(lineNum > end):
					endCode += line + "\n"
				else:
					midCode += line + "\n"	
			lineNum += 1	

		return (begCode,midCode,endCode)