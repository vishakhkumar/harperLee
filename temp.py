from sys import argv

summ = ""

f = open('text1.txt', 'r')
g = open('chapterwise.txt','w')

word = [' and ',' or ',' goes ',' her ',' him ',' he ',' she ',' the ',' from ',' a ' ,' an ','SHOT',"MOVING","BEDROOM","EXT","'"]

chapterList = [str(i) for i in range(0,303)]

charList = ["FINCH","SCOUT","JEM","JEAN Louise","REYNOLD","STEPHANIE","MAUDIE"]







for line in f:
    line = line.replace('.'," ")
    line = line.rstrip('\n')
    line = line + " "
    for i in word:
        if i in line:
           line = line.replace(i," ")
    for i in chapterList:
        if i in line:
           line = line.replace(i,'",\n"' )

    line = line.replace('"",',"")
    g.write(line)
g.close()
f.close()





f = open('text1.txt', 'r')
g = open('characterwise.txt','w')


for line in f:
    line = line.replace('.'," ")
    line = line.rstrip('\n')
    line = line + " "
    for i in word:
        if i in line:
           line = line.replace(i," ")
    for i in charList:
        if i in line:
           line = line.replace(i,'",\n\n"' )

    line = line.replace('"",',"")
    line = line.replace('.'," ")
    g.write(line)
g.close()
f.close()



f = open('tweets.txt', 'r')
g = open('tweetwise.txt','w')


for line in f:
    line = line.replace('.'," ")
    line = line.rstrip('\n')
    line = line + " "
    for i in word:
        if i in line:
           line = line.replace(i," ")
    for i in charList:
        if i in line:
           line = line.replace(i,'",\n\n"' )

    line = line.replace('"",',"")
    line = line.replace('.'," ")
    g.write(line)
g.close()
f.close()
