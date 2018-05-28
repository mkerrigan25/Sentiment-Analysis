import re
import glob   
import csv
path = 'LGWS_AMAZON.CO.UK_TXT/Review*.txt'   
files=glob.glob(path)   
stars = re.compile('(\d+)\.(\d+) out')
name =  re.compile('(\w+)(.*)(\-) See')
date =  re.compile('\d+ \w+ 20\d+')
result=[0 for x in range(59)]

x2=0
result[0]=["Name","Date","Stars","Review"]
for file in files: 
	f=open(file, 'r')
	r=[0 for x in range(4)]
	lines=f.readlines()
	x=0
	
	while(x<len(lines)):
		if(name.match(lines[x])):
			d=name.match(lines[x])
			a=d.group(0)
			a=a.split("-")
			a[0]=a[0].replace("By", "")
			r[0]=a[0].strip()
		if(date.search(lines[x])):
			d=date.search(lines[x])
			print d.group(0)
			d=d.group(0)
			r[1]=d.strip()
			
		if(stars.match(lines[x])):
			s=stars.match(lines[x])
			y=s.group(0)
			y =y[:3]
			r[2]=y.strip()
			
		if "This review is from: Let the Great World Spin" in lines[x]:
			review =lines[x+1:] 
			review="".join(review)
			r[3]=review.strip()

		#print result[x+1]
		x+=1
	x2+=1
	result[x2]=r
	#print review
	#print lines[1]
f.close()
x=0
csvfile=open('uk.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerows(result)
