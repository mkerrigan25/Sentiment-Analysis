from __future__ import print_function
from nltk.stem.wordnet import WordNetLemmatizer
import nltk.data
import re
#nltk.download()

#gives word list as an associative array, since each word in synset mapped seperatly
def dictionary():
	word =  re.compile('(\w+)#(\w)')
	with open('micrownop/Micro-WNOp-data.txt') as f:
		lines=f.readlines()
	x=7
	common={}
	g1={}
	g2={}
	a =[0 for x in range(len(lines))]
	x=8
	while(x<len(lines)): #common group
		if(x<117):
			a[x]=lines[x].split()
			j=2
			while(j<len(a[x])):
				a[x][j]= word.search(a[x][j])
				a[x][j]=a[x][j].group(0)
				
				if a[x][j] not in common:
					common.update({a[x][j]:[a[x][0],a[x][1]]})
					
				j+=1
		elif(x>=120 and x<616): #group1
			a[x]=lines[x].split()
			j=6
			while(j<len(a[x])):
				a[x][j]= word.search(a[x][j])
				a[x][j]=a[x][j].group(0)
				
				if a[x][j] not in g1:
					g1.update({a[x][j]:[a[x][0],a[x][1],a[x][2],a[x][3],a[x][4],a[x][5]]})
				
				j+=1

		elif(x>=619 and x<1118): #group2
			j=4
			
			a[x]=lines[x].split()
			while(j<len(a[x])):
				a[x][j]= word.search(a[x][j])
				a[x][j]=a[x][j].group(0)
				
				if a[x][j] not in g2:
					g2.update({a[x][j]:[a[x][0],a[x][1],a[x][2],a[x][3]]})
					
					
				j+=1
			
		x+=1
	return [common,g1,g2]

def score(words,a, b, c):
	x=0
	y=0
	neg=0
	pos=0
	obj=0
	p=0 #number of positive words
	n=0 #number of negative words
	o=0 #Number of objective words
	while(x<len(words)):
		z=0
		while(z<len(words[x])):
			w=words[x][z]
			if(w in a):
				if(float(a[w][0])>0 and float(a[w][1])==0):
					pos=float(a[w][0])+pos
					p+=1
					#return [float(a[w][0]),'p']
		
				elif(float(a[w][1])>0 and float(a[w][0])==0):
					neg=float(a[w][1])+neg
					n+=1
					#return [float(a[w][0]),'n']
		
				else:
					obj=(1.0-(float(a[w][0])+float(a[w][1])))+obj
					o+=1
			elif(w in b):
				if((float(b[w][0])+float(b[w][2])+float(b[w][4]))/3 >0 and (float(b[w][1])+float(b[w][3])+float(b[w][5]))/3 ==0):
					pos=(float(b[w][0])+float(b[w][2])+float(b[w][4]))/3+pos
					p+=1
					#return [float(a[w][0]),'p']
		
				elif((float(b[w][1])+float(b[w][3])+float(b[w][5]))/3>0 and (float(b[w][0])+float(b[w][2])+float(b[w][4]))/3==0):
					neg=(float(b[w][1])+float(b[w][3])+float(b[w][5]))/3+neg
					n+=1
					#print(w,2)
					#return [float(a[w][0]),'n']
		
				else:
					obj=(1.0-(float(b[w][1])+float(b[w][3])+float(b[w][5])+(float(b[w][0])+float(b[w][2])+float(b[w][4])))/3)+obj
					o+=1
			elif(w in c):
				if((float(c[w][0])+float(c[w][2]))/3 >0 and (float(c[w][1])+float(c[w][3]))/3 ==0):
					pos=(float(c[w][0])+float(c[w][2]))/3+pos
					p+=1
					#return [float(a[w][0]),'p']
		
				elif((float(c[w][1])+float(c[w][3]))/3>0 and (float(c[w][0])+float(c[w][2]))/3==0):
					neg=(float(c[w][1])+float(c[w][3]))/3+neg
					n+=1
					#return [float(a[w][0]),'n']
		
				else:
					obj=(1.0-(float(c[w][1])+float(c[w][3])+float(c[w][0])+float(c[w][2]))/3)+obj
					o+=1
			z+=1
		x+=1
	if(p>n and p>o):
		return (pos/p ,"positve review")
	elif(n>p and n>o):
		return (neg/n , "negative review")
	elif(o>0):
		return(obj/o ,"objective review")
	else:
		return(1, " failed")

def token(tag):
	if(tag=="JJ" or tag=="JJR" or tag=="JJS" ):
		return "#a"
	elif(tag=="NN" or tag=="NNS" or tag=="NNP" or tag=="NNPS"):
		return "#n"
	elif(tag=="RB" or tag=="RBR" or tag=="RBS"):
		return "#r"
	elif(tag=="VB" or tag=="VBD" or tag=="VBG" or tag=="VBN" or tag=="VBP" or tag=="VPZ"):
		return "#v"
	else:
		# i for ignore
		return "#i"

dic=dictionary()
def sentiment(text):
	x=0
	lines = text
	lines=lines.split(".")
	z=0
	st = WordNetLemmatizer()
	
	#lines is an array where each element is a sentence
	while(z<len(lines)):
	
		word=lines[z]
		wor=nltk.word_tokenize(word)
		result=nltk.pos_tag(wor)
		while(x<len(result)):
			#token converts Penn Treebank POS tags to wordnet tags
			
			result[x]=st.lemmatize(result[x][0]) + token(result[x][1])
					
			lines[z]=result
			
			x+=1
		z+=1
		x=0
	return score(lines,dic[0],dic[1],dic[2])






