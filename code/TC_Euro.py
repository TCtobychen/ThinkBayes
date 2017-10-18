from thinkbayes import Suite
from TC_Useful import TC_Plot
import thinkbayes
import matplotlib.pyplot as plt
class Euro(Suite):
	def Likelihood(self,data,hypo):
		x = hypo/100.0
		if data=='H':
			return x
		else :
			return 1-x

x = xrange(0,101)
euro = Euro(x)
x=1
while x <= 140:
	euro.Update('H')
	x += 1
x=1
while x <= 110:
	euro.Update('T')
	x += 1
L1=[];L2=[]
for x,y in euro.Items():
	L1.append(x);L2.append(y)
TC_Plot(L1,L2)
print thinkbayes.CredibleInterval(euro,90)
L='H'*10 + 'T'*10
print L[1:]
