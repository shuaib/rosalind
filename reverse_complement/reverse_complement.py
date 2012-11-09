s = raw_input()
s = s[::-1]
s = list(s)
news = []
for a in s:
    if a=='A':
        news.append('T')
    elif a=='T':
        news.append('A')
    elif a=='C':
        news.append('G')
    elif a=='G':
        news.append('C')

print "".join(news)
