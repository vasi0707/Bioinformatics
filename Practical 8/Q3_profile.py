import numpy as np
import matplotlib.pyplot as plt

file = open("Q2.fasta")
a = file.readlines()
seq = a[1]
file.close()

Hp = [13.85,0,15.37,11.61,11.38,13.93,13.34,13.82,15.28,0,11.58,14.13,13.86,13.02,0,12.35,12.61,13.10,13.39,12.70,0,14.56,15.48,0,13.88,0]

def window_size_9(seq,n):
    final_seq = ""
    for i in range(n-4,n+5):
        final_seq = final_seq + seq[i]
    return final_seq

def window_size_19(seq,n):
    final_seq = ""
    for i in range(n-9,n+10):
        final_seq = final_seq + seq[i]
    return final_seq

Hp_profile1 = np.zeros([len(seq)-9])
avg_Hp1 = 0
for i in range(4,len(seq)-5):
    check_seq = window_size_9(seq,i)
    for j in range(9):
        res = ord(check_seq[j]) - 65
        Hp_profile1[i-4] = Hp_profile1[i-4] + Hp[res]
    Hp_profile1[i-4] = Hp_profile1[i-4]/9
    avg_Hp1 = avg_Hp1 + Hp_profile1[i-4]

avg_Hp1 = avg_Hp1/(len(seq)-9)
plt.subplot()
plt.axhline(y=avg_Hp1)
plt.plot(Hp_profile1)
plt.xlabel('sequence')
plt.ylabel('Hydrophobicities')
plt.title('Hydrophobicity Profile (window size=9)')
plt.show()

Hp_profile2 = np.zeros([len(seq)-19])
avg_Hp2 = 0
for i in range(9,len(seq)-10):
    check_seq = window_size_19(seq,i)
    for j in range(19):
        res = ord(check_seq[j]) - 65
        Hp_profile2[i-9] = Hp_profile2[i-9] + Hp[res]
    Hp_profile2[i-9] = Hp_profile2[i-9]/19
    avg_Hp2 = avg_Hp2 + Hp_profile2[i-9]

avg_Hp2 = avg_Hp2/(len(seq)-19)
plt.subplot()
plt.axhline(y=avg_Hp2)
plt.plot(Hp_profile2)
plt.xlabel('sequence')
plt.ylabel('Hydrophobicities')
plt.title('Hydrophobicity Profile (window size=19)')
plt.show()
