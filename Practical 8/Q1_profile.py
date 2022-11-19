import numpy as np
import matplotlib.pyplot as plt

file = open("Q1.fasta")
sequences = file.readlines()
file.close()

Hp = [13.85,0,15.37,11.61,11.38,13.93,13.34,13.82,15.28,0,11.58,14.13,13.86,13.02,0,12.35,12.61,13.10,13.39,12.70,0,14.56,15.48,0,13.88,0]

for i in range(1,len(sequences),2):
    seq = sequences[i]
    Hp_profile = np.zeros([len(seq)-1])
    avg_Hp = 0
    for j in range(len(seq)-1):
        res = ord(seq[j]) - 65
        Hp_profile[j] = Hp[res]
        avg_Hp = avg_Hp + Hp[res]
    avg_Hp = avg_Hp/(len(seq)-1)
    plt.subplot()
    plt.axhline(y=avg_Hp)
    plt.plot(Hp_profile)
    plt.xlabel('sequence')
    plt.ylabel('Hydrophobicities')
    plt.title(sequences[i-1])
    plt.show()

