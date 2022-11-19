import numpy as np
import math
seq = input("Enter your sequence:")

freq = np.zeros([26])

for i in range(len(seq)):
    residue = ord(seq[i]) - 65
    freq[residue] = freq[residue] + 1

print("The frequencies of amino acid are:")
print("Alanine:",freq[0])
print("Cysteine:",freq[2])
print("Aspartic acid:",freq[3])
print("Glutamic acid:",freq[4])
print("Phenylalanine:",freq[5])
print("Glycine:",freq[6])
print("Histidine:",freq[7])
print("Isoleucine:",freq[8])
print("Lysine:",freq[10])
print("Leucine:",freq[11])
print("Methionine:",freq[12])
print("Asparagine:",freq[13])
print("Proline:",freq[15])
print("Glutamine:",freq[16])
print("Arginine:",freq[17])
print("Serine:",freq[18])
print("Threonine:",freq[19])
print("Valine:",freq[21])
print("Tryptophan:",freq[22])
print("Tyrosine:",freq[24])
print(" ")

freq_mat = (freq/len(seq))*100

print(" ")
print("The composition of amino acid are:")
print("Alanine:",freq_mat[0])
print("Cysteine:",freq_mat[2])
print("Aspartic acid:",freq_mat[3])
print("Glutamic acid:",freq_mat[4])
print("Phenylalanine:",freq_mat[5])
print("Glycine:",freq_mat[6])
print("Histidine:",freq_mat[7])
print("Isoleucine:",freq_mat[8])
print("Lysine:",freq_mat[10])
print("Leucine:",freq_mat[11])
print("Methionine:",freq_mat[12])
print("Asparagine:",freq_mat[13])
print("Proline:",freq_mat[15])
print("Glutamine:",freq_mat[16])
print("Arginine:",freq_mat[17])
print("Serine:",freq_mat[18])
print("Threonine:",freq_mat[19])
print("Valine:",freq_mat[21])
print("Tryptophan:",freq_mat[22])
print("Tyrosine:",freq_mat[24])

mol_wei = [85,0,115,130,145,160,70,150,125,0,145,125,143,130,0,110,140,170,100,115,0,110,200,0,175,0]

w = 0    
for i in range(26):
    w = w + (freq[i]*mol_wei[i])

print(" ")
w = w - (18*(len(seq)-1))
print("The molecular weight is:",w)

grp_A = [8.47,0,1.39,5.97,6.32,3.91,7.82,2.26,5.71,0,5.76,8.48,2.21,4.54,0,4.63,3.82,4.93,5.94,5.79,0,7.02,1.44,0,3.58,0]
grp_B = [8.95,0,0.47,5.91,4.78,3.68,8.54,1.25,4.77,0,4.93,8.78,1.56,5.74,0,3.74,4.75,5.24,8.05,6.54,0,6.76,1.24,0,4.13,0]

stdA = 0
for i in range(26):
    stdA = stdA + (abs(grp_A[i]-freq_mat[i]))

stdB = 0
for i in range(26):
    stdB = stdB + (abs(grp_B[i]-freq_mat[i]))

print(" ")
print("stdA:",stdA)
print(" ")
print("stdB:",stdB)
print(" ")
if(stdA<stdB):
    print("The protein sequence belongs to: GROUP A")
elif(stdA>stdB):
    print("The protein sequence belongs to: GROUP B")
else:
    print("Group A and Group B")
