#!/usr/bin/python

import numpy as np

a1 = np.array([0,0,0])
a2 = np.array([0,.167,0.167])
atpos = []

def onecheck(a,b):
    c = []
    for i in range(len(a)):
        if a[i] < 1:
            if b[i] < 1:
                c.append(1)
    if len(c) == len(a):
        return True

atpos.append(a1)
atpos.append(a2)

for i in range(3):
    b = [0,0,0]
    b[i] = 0.333
    for j in range(3):
        a = [0,0,0]
        a[j] = 0.333
        ta1 = a1 + a
        ta2 = a2 + a
        if onecheck(ta1,ta2) == True:
            atpos.append(ta1)
            atpos.append(ta2)
    for j in range(3):
        a = [0.333,0.333,0.333]
        a[j] = 0
        ta1 = a1 + a
        ta2 = a2 + a
        if onecheck(ta1,ta2) == True:
            atpos.append(ta1)
            atpos.append(ta2)
    a1 = a1 + b
    a2 = a2 + b

np.savetxt('atpos.txt',atpos,fmt='%4.2f',newline='\n Al ')
