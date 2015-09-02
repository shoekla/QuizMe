quizes=[]
comments={}
def addComment(name,content):
	try:
		pastComments=comments[name]
		pastComments.append(content)
		comments.update({name:pastComments})
	except:
		comments.update({name:[content]})

def getComments(name):
	try:
		return comments[name]
	except:
		return ["No Comments so far"]#Default
def addQuiz(name,questions,answers,points,creatorName,topic,aboutQ,length):
	quizes.append([name,questions,answers,points,creatorName,topic,aboutQ,length])
def getAllQuizes():
	return quizes
def getQ(name):
	for item in quizes:
		if str(item[0])==str(name):
			return item[1]
	return ["No Questions For this Quiz"]
def getA(name):
	for item in quizes:
		if str(item[0])==str(name):
			return item[2]
	return ["No answers For this Quiz"]

def getP(name):
	for item in quizes:
		if str(item[0])==str(name):
			return item[3]
	return ["No Points For this Quiz"]

def getCr(name):
	for item in quizes:
		if str(item[0])==str(name):
			return item[4]
	return ["No creators For this Quiz"]

def getT(name):
	for item in quizes:
		if str(item[0])==str(name):
			return item[5]
	return ["No Questions For this Quiz"]

def getAbout(name):
	for item in quizes:
		if str(item[0])==str(name):
			return item[6]
	return ["No Questions For this Quiz"]

def getLen(name):
	for item in quizes:
		if str(item[0])==str(name):
			return item[7]
	return ["No Questions For this Quiz"]








