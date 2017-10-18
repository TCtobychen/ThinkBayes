from thinkbayes import Beta
beta = Beta()
beta.Update((140,110))
print beta.Mean()