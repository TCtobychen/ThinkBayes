from thinkbayes import Pmf,Cdf
from thinkbayes import Suite
import matplotlib.pyplot as plt
class Train(Suite):
	def __init__(self,hypos):
		Pmf.__init__(self)
		for hypo in hypos:
			self.Set(hypo,1.0/hypo)

	def Likelihood(self,data,hypo):
		if hypo<data:
			return 0
		else :
			return 1.0/hypo

hypos = xrange(1,1001)
suite = Train(hypos)
suite.Update(60)
L1=[];L2=[]
for x,y in suite.Items():
	L1.append(x);L2.append(y)
'''plt.plot(L1,L2)
plt.axis([0,1000,0,0.02])
plt.show()'''
print suite.Mean()
cdf = suite.MakeCdf()
interval = cdf.Percentile(5),cdf.Percentile(95)
print interval