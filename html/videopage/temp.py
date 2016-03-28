from sys import argv

summ = ""

f = open('text1.txt', 'r')
g = open('result1.txt','w')

for line in f:
   line = line.rstrip('\n')
   line = line + " "
   line.replace("\0", " ")
   summ = summ + line

print summ

g.write(summ)

f.close()
g.close()
