from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
import time
import quiz
import scrape
import os
app = Flask(__name__)
"""
quizes=[]

class Quiz:
	def __init__(self, name, questions,answers,points,creatorName,topic,aboutQ):
		self.name=name
		self.questions=questions
		self.answers=answers
		self.points=points
		self.creatorName=creatorName
		self.topic=topic
		self.aboutQ=aboutQ
	def getLen():
		return len(self.questions)
	def getQuestions():
		return self.questions
	def getAnswers():
		return self.answers
	def getPoints():
		return self.points
	def getCreator():
		return self.creatorName
	def getTopic():
		return self.topic
	def getName():
		return self.name
"""
@app.route('/')
def my_form():
	return render_template("index.html")


@app.route('/add')
def addQ():
	return render_template("add1.html")

lenght=0;
@app.route('/add/partA', methods=['POST'])
def my_form_post(name=None,numQ=None,creatorName=None,topic=None,length=0,aboutQ=None,message=None):
	name = request.form['name']
	numQ = request.form['numQ']
	topic= request.form['topic']
	creatorName = request.form['creatorName']
	aboutQ=request.form['aboutQ']
	try:
		length=int(numQ)
	except:
		message="Number of Questions must be a number"
		return render_template("add1.html",message=message)
	return render_template("add2.html",length=length,name=name,creatorName=creatorName,topic=topic,aboutQ=aboutQ)

@app.route('/add/partB', methods=['POST'])
def qContent(questions=[],answers=[],points=[],name=None,length=0,topic=None,creatorName=None,aboutQ=None,score=0,message=None):
	questions=[]
	answers=[]
	score=0
	points=[]
	topic=request.form['topic']
	aboutQ=request.form['aboutQ']
	creatorName=request.form['creatorName']
	name=request.form['name']
	length=int(request.form['length'])
	for i in range(0,length):
		questions.append(request.form['q'+str(i)])
		answers.append(request.form['a'+str(i)])
		points.append(request.form['p'+str(i)])
	try:
		for item in points:
			score=score+int(item)
		if score!=100:
			message="Scores must add up to 100"
			return render_template("add2.html",length=length,name=name,creatorName=creatorName,topic=topic,aboutQ=aboutQ,message=message)

	except:
		message="Scores must be numbers"
		return render_template("add2.html",length=length,name=name,creatorName=creatorName,topic=topic,aboutQ=aboutQ,message=message)

	quiz.addQuiz(name,questions,answers,points,creatorName,topic,aboutQ,length)
	return render_template("conf.html",name=name,topic=topic,creatorName=creatorName,answers=answers,questions=questions,points=points,aboutQ=aboutQ)

@app.route('/searchHome')
def sa(x=[]):
	x=[]
	x=quiz.getAllQuizes()
	length=len(x)
	return render_template("searchHome.html",x=x,length=length)
@app.route('/topic/<name>')
def greet(name):
	return render_template("topicHome.html",name=name)
@app.route('/topic/links/<name>')
def findL(name,res=[],length=None):
	res=[]
	res=scrape.SearchCrawl(name)
	length=len(res)
	return render_template("links.html",length=length,res=res,name=name)
@app.route('/topic/vids/<name>')
def vidL(name,res=[],length=None):
	res=[]
	res=scrape.getVideoSearch(name)
	length=len(res)
	return render_template("vids.html",name=name,res=res,length=length)
@app.route('/quizHome/<name>')
def quizH(name,about=None,topic=None,length=None,creator=None,comments=[]):
	try:
		comments=[]
		about=quiz.getAbout(name)
		topic=quiz.getT(name)
		creator=quiz.getCr(name)
		length=quiz.getLen(name)
		comments=quiz.getComments(name)
		return render_template("quizHome.html",name=name,topic=topic,about=about,length=length,creator=creator,comments=comments)
	except:
		return "<h1>This Quiz does not exist yet</h1>"
@app.route('/quiz/<name>')
def actQuiz(name,questions=[],topic=[],length=0,creator=None):
	try:
		questions=quiz.getQ(name)
		topic=quiz.getT(name)
		length=quiz.getLen(name)
		creator=quiz.getCr(name)
		return render_template("quiz.html",name=name,questions=questions,topic=topic,length=length,creator=creator)
	except:
		return "Error Occurred"
@app.route('/grade', methods=['POST'])
def grade(name=None,userA=[],points=[],answers=[],ans=None,score=0,questions=[],topic=None,creator=None):
	userA=[]
	questions=[]
	answers=[]
	score=0
	points=[]
	name=request.form['name']
	topic=request.form['topic']
	creator=request.form['creator']
	questions=quiz.getQ(name)
	points=quiz.getP(name)
	answers=quiz.getA(name)
	for i in range(0,len(answers)):
		ans=request.form['a'+str(i)]
		userA.append(ans)
	for i in range(0,len(answers)):
		if str(userA[i]).lower()==str(answers[i]).lower():
			score=score+int(points[i])
	return render_template("grade.html",score=score,userA=userA,answers=answers,questions=questions,name=name,topic=topic,creator=creator)

@app.route('/comment/<name>')
def com(name):
	return render_template("comment.html",name=name)
@app.route('/Add/comment/<name>', methods=['POST'])
def comm(name=None,newComment=None):
	name=request.form['name']
	newComment=request.form['newComment']
	quiz.addComment(name,newComment)
	return redirect("/quizHome/"+str(name))

@app.route('/about')
def about():
	return redirect('https://plus.google.com/107108771936096317653/posts')


if __name__ == '__main__':
    app.run()

