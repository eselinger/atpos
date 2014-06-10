#!/usr/bin/python

import numpy as np

size = 15
a = size/7.50
b = 1/a
atpos = []

a1 = np.array([0,0,0]) #origin atom
a2 = np.array([0,0.25,0.25]) #face atom on y
a3 = np.array([0.25,0,0.25]) #face atom on x

print b

for k in range (int(a)): #loop through x
    atpos.append(a1)
    atpos.append(a2)
    atpos.append(a3)
    ta1 = a1
    ta2 = a2
    ta3 = a3
    for i in range(int(a)): #loop through y
        tta1 = ta1
        tta2 = ta2
        tta3 = ta3
        for j in range(int(a)-1): #loop through z
            tta1 = tta1 + [0,b,0]
            tta2 = tta2 + [0,b,0]
            tta3 = tta3 + [0,b,0]
            atpos.append(ta1)
            atpos.append(ta2)
            atpos.append(ta3)
        ta1 = ta1 + [0,0,b]
        ta2 = ta2 + [0,0,b]
        ta3 = ta3 + [0,0,b]
        atpos.append(ta1)
        atpos.append(ta2)
        atpos.append(ta3)
    a1 = a1 + [b,0,0]
    a2 = a2 + [b,0,0]
    a3 = a3 + [b,0,0]
 
np.savetxt('atpos.txt',atpos,fmt='%4.2f',newline='\n Al ')
