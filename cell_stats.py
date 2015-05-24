#!/usr/bin/env python
import numpy as np
import sys




dt=np.dtype({'names':['start','end','CellId','IMSI','RNTI','LCID','nTxPDUs','TxBytes','nRxPDUs','RxBytes','delay','stdDev'],'formats':[np.float,np.float,np.float,np.float,np.float,np.float,np.float,np.float,np.float,np.float,np.float,np.float]})
a = np.loadtxt(open('DlRlcStats.txt'),dtype=dt,comments='%')
y=a['start']
z=a['TxBytes']*8
mi=min(y)
rate=0;
x=[]

# Calcul rate celulle,
for k in range(len(y)):		
	if y[k] == mi:
		rate = rate + z[k]	
		if k == len(y):
			x.append(rate)		
	else :
		mi=mi+1
		x.append(rate)
		rate=z[k]
	k=k+1


#x=y[3::]
#x.sort()

print len(x)

# t = 30000000
# pas= 400000
# cdfrate = [0]*(50)
# frate = [0]*(50)
# n=0
# for j in range(50) :
	# frate[j]=t
	
	# for i in range(len(x)) :   
		# if x[i]>= t and x[i] <= (t+pas) :
			# n=n+1	       
		# cdfrate [j] = n;	
		# i=i+1
	# t=t+pas
	# j=j+1

	

# if str(sys.argv[2]) == "1":
		# np.savetxt(str(sys.argv[1]), np.column_stack((frate,cdfrate))) 
# else:
		# b = np.loadtxt(open(str(sys.argv[1])),comments='%')
		# np.savetxt(str(sys.argv[1]), np.column_stack((b,cdfrate)))

if str(sys.argv[2]) == "1":
		np.savetxt(str(sys.argv[1]), np.column_stack(x)) 
else:
		b = np.loadtxt(open(str(sys.argv[1])),comments='%')
		np.savetxt(str(sys.argv[1]), np.column_stack((b,x)))		
		
		

		
