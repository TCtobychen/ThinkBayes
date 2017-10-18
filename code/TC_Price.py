import csv
import numpy
import thinkbayes

def ReadData(filename='showcases.2011.csv'):
    fp = open(filename)
    reader = csv.reader(fp)
    res = []

    for t in reader:
        _heading = t[0]
        data = t[1:]
        try:
            data = [int(x) for x in data]
            # print heading, data[0], len(data)
            res.append(data)
        except ValueError:
            pass
    fp.close()
    return zip(*res)

prices=ReadData()
pdf=thinkbayes.EstimatedPdf(prices)
'''low,high = 0,75000
n=101
xs=numpy.linspace(low,high,n)
pmf=pdf.MakePmf(xs)
for x,y in pmf.Items():
	print x,y'''
