import csv
import re
f = open('us.csv')
a= []
files = csv.reader(f)
for row in files:
	a.append(row)
i=1
failed=0
correct=0
total=len(a)-1
print (total)
while(i<len(a)):
	if((float(a[i][2])>=0 and float(a[i][2])<=2) and ( a[i][5]=="negative review")):
		correct+=1
	elif((float(a[i][2])>=2 and float(a[i][2])<=4) and a[i][5]=="objective review"):
		correct+=1
	elif((float(a[i][2])>=4 and float(a[i][2])<=5) and ( a[i][5]=="positive review")):
		correct+=1
	
	elif(a[i][5]==" failed"):
		total-=1
		failed+=1
	i+=1
print (failed, " Failed reviews")
print ((float(failed)/float(len(a)-1))*100, "Percent failed")
print (total, " Successful reviews")
print ((float(total)/float(len(a)-1))*100, "Success")
print (correct, " correct reviews")
print ((float(correct)/float(total))*100, "Percent correct")