import numpy as np
import math
seq = input("Enter your sequence:")

freq = np.zeros([26])

for i in range(len(seq)):
    residue = ord(seq[i]) - 65
    freq[residue] = freq[residue] + 1

freq_mat = (freq/len(seq))*100
p = np.zeros([26,26],dtype=float)
a = np.zeros([26,26],dtype=float)
b = np.zeros([26,26],dtype=float)
c = np.zeros([26,26],dtype=float)

for i in range(1,len(seq)):
    res1 = ord(seq[i-1]) - 65
    res2 = ord(seq[i]) - 65
    p[res1][res2] = p[res1][res2] + 1

for i in range(26):
    for j in range(26):
        if((freq[i]!=0) or (freq[j]!=0)):
            a[i][j] = (p[i][j]*100)/(freq[i]+freq[j])
        b[i][j] = (p[i][j]*100)/(len(seq)-1)
        if((freq[i]!=0) and (freq[j]!=0)):
            c[i][j] = (p[i][j]*100)/(freq[i]*freq[j])

print("4(a)")
for i in range(26):
    for j in range(26):
        if((j!=1) and (j!=9) and (j!=14) and (j!=20) and (j!=23) and (j!=25) and (i!=1) and (i!=9) and (i!=14) and (i!=20) and (i!=23) and (i!=25)):
            print("%.2f" % a[i][j],end="  ")
            if(j==24):
                print(" ")
print(" ")
print(" ")

print("4(b)")
for i in range(26):
    for j in range(26):
        if((j!=1) and (j!=9) and (j!=14) and (j!=20) and (j!=23) and (j!=25) and (i!=1) and (i!=9) and (i!=14) and (i!=20) and (i!=23) and (i!=25)):
            print("%.2f" % b[i][j],end="  ")
            if(j==24):
                print(" ")

print(" ")
print(" ")

print("4(c)")
for i in range(26):
    for j in range(26):
        if((j!=1) and (j!=9) and (j!=14) and (j!=20) and (j!=23) and (j!=25) and (i!=1) and (i!=9) and (i!=14) and (i!=20) and (i!=23) and (i!=25)):
            print("%.2f" % c[i][j],end="  ")
            if(j==24):
                print(" ")
