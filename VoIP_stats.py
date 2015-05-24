#!/usr/bin/env python
import numpy as np
import sys




dt=np.dtype({'names':['Time','Delay','PacketSize','Data-Rate','RNTI','ID-Source','Start'],'formats':[np.float,np.float,np.float,np.float,np.float,np.float,np.float]})

a = np.loadtxt(open('DPI-184_stats.txt'),dtype=dt,comments='%')


y=a['Time']
w=a['Delay']*1000
m=a['RNTI']
z=a['PacketSize']*8
ss= set(m)
mi=int(min(y))
rate=0;
x=[]

for ni in range(len(ss)):
	ui=ss.pop()
	for k in range(len(y)):	
		if y[k] <= mi and m[k]==ui:
			rate = rate + z[k]		       
		elif m[k]==ui:
			mi=mi+1
			if(rate>1000):			
				x.append(rate) 
			rate=z[k]
	
			
		k=k+1
	mi=min(y)+1
	ni=ni+1


#x=y[3::]
x.sort() 
print len(x)
#print x

pas= 1000
cdfrate = []
frate = []
t = 0
ma=0
n=0

while t<int(min(x)):
	ma=ma+1
	cdfrate.append(n);
	frate.append(t);
	t=t+pas	
t=t-pas
for j in range(len(x)) :

	if x[j] >= t and x[j]<(t+pas):
		n=n+1
	else :
		if ma<200:
			var = True
			while var or x[j] > (t+pas):
				t=t+pas
				ma=ma+1
				cdfrate.append(n)
				frate.append(t)
				var = False
		n=n+1	
	j=j+1
	if j == len(x) and ma<200:
		t=t+pas
		cdfrate.append(n)
		frate.append(t)
	


while ma<200:
	t=t+pas
	ma=ma+1
	cdfrate.append(max(cdfrate));
	frate.append(t);





if str(sys.argv[2]) == "1":
		np.savetxt(str(sys.argv[1]), np.column_stack((frate,cdfrate))) 
else:
		b = np.loadtxt(open(str(sys.argv[1])),comments='%')
		np.savetxt(str(sys.argv[1]), np.column_stack((b,cdfrate)))
		
		
		
#	Calcul Delay
w.sort() 
cdfdelay = []
fdelay = []
t = 0
pas= 1
ma=0
n=0

while t<int(min(w)):
	cdfdelay.append(n);
	fdelay.append(t);
	t=t+pas	
	ma=ma+1
t=t-pas
for j in range(len(w)) :

	if w[j] >= t and w[j]<(t+pas):
		n=n+1
	else :
		if ma<200:
			var = True
			while var or w[j] > (t+pas):
				t=t+pas
				ma=ma+1
				cdfdelay.append(n)
				fdelay.append(t)				
				var = False
		n=n+1	
	j=j+1
	if j == len(w) and ma<200 :
		t=t+pas
		cdfdelay.append(n)
		fdelay.append(t)


while ma<200:
	t=t+pas
	ma=ma+1
	cdfdelay.append(max(cdfdelay));
	fdelay.append(t);	

	

if str(sys.argv[2]) == "1":
		np.savetxt(str(sys.argv[3]), np.column_stack((fdelay,cdfdelay))) 
else:
		b = np.loadtxt(open(str(sys.argv[3])),comments='%')
		np.savetxt(str(sys.argv[3]), np.column_stack((b,cdfdelay)))
	

if str(sys.argv[2]) == "1":
		np.savetxt(str(sys.argv[4]), np.column_stack((w))) 
else:
		b = np.loadtxt(open(str(sys.argv[4])),comments='%')
		c= b.tolist()+w
		c.sort() 
		np.savetxt(str(sys.argv[4]), np.column_stack(c))
	


		
