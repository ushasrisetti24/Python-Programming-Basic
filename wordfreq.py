frq= {}
line= input()

for word in line.split():
    frq[word]= set(word,0)+1

words= frq.keys()
words.sort()

for w in words:
    print("%s : %d" %(w,frq[w]))
