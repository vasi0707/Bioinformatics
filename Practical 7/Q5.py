import numpy as np
import math
seq = input("Enter your sequence:")

freq = np.zeros([26])

for i in range(len(seq)):
    residue = ord(seq[i]) - 65
    freq[residue] = freq[residue] + 1

Hgm = [13.85,0,15.37,11.61,11.38,13.93,13.34,13.82,15.28,0,11.58,14.13,13.86,13.02,0,12.35,12.61,13.10,13.39,12.70,0,14.56,15.48,0,13.88,0]
Ca = [20.00,0,25.00,26.00,33.00,46.00,13.00,37.00,39.00,0,46.00,35.00,43.00,28.00,0,22.00,36.00,55.00,20.00,28.00,0,33.00,61.00,0,46.00,0]
Et = [1.90,0,2.04,1.52,1.54,1.86,1.90,1.76,1.95,0,1.37,1.97,1.96,1.56,0,1.70,1.52,1.48,1.75,1.77,0,1.98,1.87,0,1.69,0]

hydrophobicity = 0
helix = 0
energy = 0

for i in range(26):
    hydrophobicity = hydrophobicity + (freq[i]*Hgm[i])
    helix = helix + (freq[i]*Ca[i])
    energy = energy + (freq[i]*Et[i])

average_hydrophobicity = hydrophobicity/len(seq)

print("Average hydrophobicity:",average_hydrophobicity)
print("Helical contact area:",helix)
print("Total non-bonded energy:",energy)
