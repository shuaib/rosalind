s = raw_input()
s = list(s)
news = [w.replace('T', 'U') for w in s]
print "".join(news)
