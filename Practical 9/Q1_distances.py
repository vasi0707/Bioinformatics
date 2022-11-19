import numpy as np
import math

seq1 = "AMENLNMDLLYMAAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA"
seq2 = "AADVSAAVGATGQSGMTYRLGLSWDWDKSWWQTSTGRLTGYWDAGYTYWEGGDEGAGKHSLSFAPVFVYEFAGDSIKPFIEAGIGVAAFSGTRVGDQNLGSSLNFEDRIGAGLKFANGQSVGVRAIHYSNAGLKQPNDGIESYSLFYKIPI"
seq3 = "MALLPAAPGAPARATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPSLHHATATPEYLAALKQKSRHAA"

sequences = [seq1,seq2,seq3]

freq = np.zeros([3,26])

count = 0

while(count<3):
    seq = sequences[count]
    for i in range(len(seq)):
        residue = ord(seq[i]) - 65
        freq[count][residue] = freq[count][residue] + 1
    count = count + 1

freq[0][:] = freq[0][:]/len(seq1)
freq[1][:] = freq[1][:]/len(seq2)
freq[2][:] = freq[2][:]/len(seq3)

ham_dist = [0,0,0]

for i in range(26):
    ham_dist[0] = ham_dist[0] + abs(freq[0][i]-freq[1][i])
for i in range(26):
    ham_dist[1] = ham_dist[1] + abs(freq[0][i]-freq[2][i])
for i in range(26):
    ham_dist[2] = ham_dist[2] + abs(freq[1][i]-freq[2][i])

print("Hamming distance between sequences 1 and 2:",ham_dist[0])
print("Hamming distance between sequences 1 and 3:",ham_dist[1])
print("Hamming distance between sequences 2 and 3:",ham_dist[2])
print(" ")

euc_dist = [0,0,0]

for i in range(26):
    euc_dist[0] = euc_dist[0] + (abs(freq[0][i]-freq[1][i])*abs(freq[0][i]-freq[1][i]))
euc_dist[0] = math.sqrt(euc_dist[0]) 
for i in range(26):
    euc_dist[1] = euc_dist[1] + (abs(freq[0][i]-freq[2][i])*abs(freq[0][i]-freq[2][i]))
euc_dist[1] = math.sqrt(euc_dist[1])
for i in range(26):
    euc_dist[2] = euc_dist[2] + (abs(freq[1][i]-freq[2][i])*abs(freq[1][i]-freq[2][i]))
euc_dist[2] = math.sqrt(euc_dist[2])

print(" ")
print("Euclidean distance between sequences 1 and 2:",euc_dist[0])
print("Euclidean distance between sequences 1 and 3:",euc_dist[1])
print("Euclidean distance between sequences 2 and 3:",euc_dist[2])

