from thinkbayes import Cdf,Pmf,SampleSum
import scipy
'''pmf=Pmf()
for x in [1,2]:
	pmf.Set(x,1)
pmf.Normalize()
pmf.Mult(1,0.75)
pmf.Mult(2,0.5)
for hypo,prob in pmf.Items():
	print hypo,prob'''
class Die(Pmf):
	def __init__(self,sides):
		Pmf.__init__(self)
		for x in xrange(1,sides+1):
			self.Set(x,1)
		self.Normalize()
'''d6=Die(6)
d8=Die(8)
mix = Pmf()
for die in [d6,d8]:
	for outcome,prob in die.Items():
		mix.Incr(outcome,prob)
mix. Normalize()
for x,y in mix.Items():
	print x,y'''


