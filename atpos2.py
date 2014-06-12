#!/usr/bin/python

import numpy as np

size = 22.50
a = size/7.50
b = 1/a
atpos = []

"""def unique(a):
    order = np.lexsort(a.T)
    a = a[order]
    diff = np.diff(a, axis=0)
    ui = np.ones(len(a), 'bool')
    ui[1:] = (diff != 0).any(axis=1)
    return a[ui]
"""
a0 = np.array([0,0,0])
c = [[0,0,0],[b,0,0],[0,b,0],[0,0,b]]

for m in range(4): #for [0,0,0], [b,0,0], [0,b,0], [0,0,b]
    a1 = a0 + c[m]
    for l in range(int(a)): #adding b+b (e.g. [b+b,0,0])
        atpos.append(a1)
        sa1 = a1
        for k in range(int(a)*2): #loop through x
            ta1 = sa1
            for i in range(int(a)*2): #loop through y
                tta1 = ta1
                for j in range(int(a)*2): #loop through z
                    tta1 = tta1 + [b/2,0,b/2]
                    atpos.append(tta1)
                ta1 = ta1 + [0,b/2,b/2]
                atpos.append(ta1)
            sa1 = sa1 + [b/2,b/2,0]
            atpos.append(sa1)
        a1 = a1 + a1

atpos = np.array(atpos)

atpos = atpos[atpos[:,0]<0.999,:]
atpos = atpos[atpos[:,1]<0.999,:]
atpos = atpos[atpos[:,2]<0.999,:]

"""atpost = unique(atpos)

d = []

for i in range(len(atpos)): #removing any repeated permutations
    for j in range(len(atpos)):
        if i != j:
            if atpos[i] != atpos[j]:
                atpos[i] = atpos[i]
            else:
                atpos[i] = [0,0,0]
        else: atpos[i] = atpos[i]
    if atpos[i] != [0,0,0]:
        d.append(atpos[i])
"""
print len(atpos)
np.savetxt('atpos.txt',atpos,fmt='%4.2f',newline='\n Al ')
