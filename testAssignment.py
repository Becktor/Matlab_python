import os
import numpy as np
import matplotlib.pyplot as plt 
def head(): ## main function directs user to the right function dependent on keypress
	notrun = False
	os.system('CLS')
	data = 0
	while not notrun:
		print ("What would you like to do? \n1) Load Data\n2) Filter Data \n3) Show Statistic\n4) Generate diagrams\n5) end")	
		keyPressed = int(input())
		print(keyPressed)
		if keyPressed == 1:
			x = input("Please enter a filename: ")
			data=dataLoad(x)
			os.system('CLS')
			print("data loaded \n")
		elif keyPressed == 2:
			# add filter data, data is a list of triples
			print("todo")
		elif keyPressed == 3:
			s = input("Please enter a statistic: ")
			print(dataStatistics(data,s))
			input("\npress any key to continue")
		elif keyPressed == 4:
			if data!=0:
				dataPlot(data)
				os.system('CLS')
				print("data plotted")
			else:
				os.system('CLS')
				print("Please load some data fist\n")
		elif keyPressed  ==5:
			print("ending")
			notrun = True

		#

def whatBakteria(d): 
	b="error"
	if d==1:
		b="Salmonella enterica"
	elif d==2:
		b="Bacillus cereus"
	elif d==3:
		b="Listeria"
	elif d==4:
		b="Brochothrix thermosphacta"
	return b

def isBakteria(d):
	b=False
	if d==1:
		b=True
	elif d==2:
		b=True
	elif d==3:
		b=True
	elif d==4:
		b=True
	return b

def dataLoad(filename):
	with open(filename) as f:
		content = f.readlines()
	data=[]
	cntr=0;
	for c in content:
		k=c.split()
		t=float(k[0])
		g=float(k[1])
		b=int(k[2])
		if t >60:
			print("On line %i, temparature too high temp on %f"%(cntr, t))
		elif t <10:
			print("On line %i, temparature too low temp on %f"%(cntr, t))
		elif g<0:
			print("On line %i, growth negative on %f"%(cntr, g))
		elif isBakteria(b)==False:
			print("On line %i, not a correct bacteria id %i"%(cntr, b))
		else:
			data.append((t,g,b))
		
		cntr=cntr+1
	
	
	return data

def dataStatistics(data, statistic):
	result = "Wrong statistic"
	if statistic=="Mean Temperature":
		t=[]
		for temp in data:
			t.append(temp[0])
		return np.mean(t)
	elif statistic=="Mean Growth rate":
		g=[]
		for growth in data:
			g.append(growth[1])
		return np.mean(g)
	elif statistic=="Std Temperature":
		t=[]
		for temp in data:
			t.append(temp[0])
		return np.std(t)
	elif statistic=="Std Growth rate":
		g=[]
		for growth in data:
			g.append(growth[1])
		return np.std(g)
	elif statistic=="Rows":
		return len(data)
	elif statistic=="Mean Cold Growth rate":
		t=[]
		for temp in data:
			if temp[0]<20:
				t.append(temp[0])
			
		return np.mean(t)
	elif statistic=="Mean Hot Growth rate":
		t=[]
		for temp in data:
			if temp[0]>50:
				t.append(temp[0])
		return np.mean(t)
	print(result)
	return result

def autolabel(rects):
	    # attach some text labels
	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
	                ha='center', va='bottom')

def dataPlot(data):
	t1 = []
	t2 = []
	t3 = []
	t4 = []
	g1 = []
	g2 = []
	g3 = []
	g4 = []
	for bacteria in sorted(data):
		if bacteria[2] == 1:
			t1.append(bacteria[0])
			g1.append(bacteria[1])
		elif bacteria[2] == 2:
			t2.append(bacteria[0])
			g2.append(bacteria[1])
		elif bacteria[2] == 3:
			t3.append(bacteria[0])
			g3.append(bacteria[1])
		elif bacteria[2] == 4:
			t4.append(bacteria[0])
			g4.append(bacteria[1])

	fig = plt.figure()
	ax = fig.add_subplot(111)

	## the data
	N = 4
	menMeans = [len(t1), len(t2), len(t3), len(t4)]
	#print("1:%i 2:%i 3:%i 4:%i"%(len(t1), len(t2), len(t3), len(t4)))

	## necessary variables
	ind = np.arange(N)                # the x locations for the groups
	width = 0.35                      # the width of the bars

	## the bars
	rects1 = ax.bar(ind, menMeans, width,color='black')
	# axes and labels
	ax.set_xlim(-width,len(ind)-width)
	ax.set_ylim(0,35)
	ax.set_ylabel('number of bacteria')
	ax.set_title('Bacteria chart')
	xTickMarks = ["1","2","3","4"]
	ax.set_xticks(ind+width/2)
	xtickNames = ax.set_xticklabels(xTickMarks)
	plt.setp(xtickNames, rotation=0, fontsize=14)
	plt.savefig("box")
	plt.show()
	
	p1=plt.plot(t1,g1)
	plt.setp(p1, color='r', linewidth=3.0)
	#print(sorted(t1))
	#print(g1)
	p2=plt.plot(t2,g2)
	plt.setp(p2, color='blue', linewidth=3.0)
	p3=plt.plot(t3,g3)
	plt.setp(p3, color='g', linewidth=3.0)
	p4=plt.plot(t4,g4)
	plt.setp(p4, color='black', linewidth=3.0)
	plt.axis([10,60,0,1])
	plt.xlabel('Temperature')
	plt.ylabel('Growth')
	plt.title('Graph for bacteria 1-4')
	plt.savefig("graph")
	plt.show()
	

if __name__ == '__main__':
	"""Tool for manual assitance in decryption of a substitution ciphertext.
    Possible to get analysis of both ciphertext and from the english language"""
	os.system('CLS')

	print ("Hello! \nWelcome to arange assistance tool! How may I help you?")
	print ("1) analyse")
	print ("0) Exit")

	keyPressed = int(input("Please select: "))

	if keyPressed == 0:
		exit
	elif keyPressed == 1:
		head()
	else:
		print ("Exiting")


#dataPlot(dataLoad("testFile3.dat"))

#print(dataStatistics(dataLoad("testFile3.dat"),"Mean Temperature"))
