#!/usr/bin/python

import itertools

a = list(itertools.permutations([0,0,0.25,0.25,0.50,0.50,0.75,0.75], 3)) #all permutations for combinations of 3 with repeating up to 2 times
b = list(itertools.permutations([0.25,0.25,0.25,0.75,0.75,0.75], 3)) #don't want any combinations of only these numbers, this would give body atom
c = []
d = []

for i in range(len(a)): #removing the b combinations
    for j in range(len(b)):
        if a[i] != b[j]:
            a[i] = a[i]
        else:
            a[i] = [0,0,0]
    
    if a[i] != [0,0,0]:
        c.append(a[i])

for i in range(len(c)): #removing any repeated permutations
    for j in range(len(c)):
        if i != j:
            if c[i] != c[j]:
                c[i] = c[i]
            else:
                c[i] = [0,0,0]
        else: c[i] = c[i]
    if c[i] != [0,0,0]:
        d.append(c[i])

f = open('atpos.txt','w') #write to outfile with name of element to copy into input file for QE
for i in range(len(d)):
    f.write(' Al' + ' ')
    for element in d[i]: f.write(str(element) + ' ')
    f.write('\n')

print len(d)
