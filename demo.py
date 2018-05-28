import csv
import sentiment_analysis
f = open('us.csv')
a= []
files = csv.reader(f)
for row in files:
	a.append(row)
i=1
while(i<len(a)):
	#print(i)
	x=sentiment_analysis.sentiment(a[i][3])
	a[i].append(x[0])
	a[i].append(x[1])

	i+=1
csvfile=open('us.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerows(a)