import matplotlib.pyplot as plt
def TC_Plot(L1,L2):
	plt.plot(L1,L2)
	L1.sort()
	L2.sort()
	plt.axis([0,L1[-1],0,L2[-1]*1.5])
	plt.show()

