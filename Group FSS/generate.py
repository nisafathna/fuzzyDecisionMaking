import random
import csv

n = input("Enter the number of parameters: ")
parameters = []
nn = n
while(n):
	parameter = raw_input("Enter parameter : ") 
	parameters.append(parameter)
	n-=1
n = nn
m = input("Enter the number of values you want to randomly generate : ")
judges = input("Enter the number of judges you want : ")

judgeSet = []

for u in xrange(judges):
	fuzzySet = []
	for i in xrange(m):
		temp = []
		for j in xrange(n):
			r = "%.2f"%random.random()
			temp.append(r)
		fuzzySet.append(temp)
	judgeSet.append(fuzzySet)

print fuzzySet

for u in xrange(judges):
	with open('judge' + str(u) + '.csv', 'wb') as csvfile:
	    spamwriter = csv.writer(csvfile, delimiter=',',
	                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    spamwriter.writerow(parameters)
	    for each in judgeSet[u]:
	    	spamwriter.writerow(each)