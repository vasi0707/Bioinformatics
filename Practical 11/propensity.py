import numpy as np
import math

sequence = "LGASGIAAFAFGSTAILIILFNMAAEVHFDPLQFFRQFFWLGLYPPKAQYGMGIPPLHDGGWWLMAGLFMTLSLGSWWIRVYSRARALGLGTHIAWNFAAAIFFVLCIGCIHPTLVGSWSEGVPFGIWPHIDWLTAFSIRYGNFYYCPWHGFSIGFAYGCGLLFAAHGATILAVARFGGDREIEQITDRGTAVERAALFW"
sec_stru = "XHHHHHHHHHHHHHHHHHHHHHHHHHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHXXHHHHHHHHHHHHHHHHHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXHHHHHHHHHHHHHHHHHHHHHHHHHHXXXXXXXXXXXXXXXXXXXXXXXXXXX"

freq_mat = np.zeros([26])
freq_mat_alpha = np.zeros([26])

for i in range(len(sequence)):
    residue = ord(sequence[i]) - 65
    freq_mat[residue] = freq_mat[residue] + 1
    if(sec_stru[i]=='H'):
        freq_mat_alpha[residue] = freq_mat_alpha[residue] + 1

propensity = np.zeros([26])
percen_helix = sum(freq_mat_alpha)/len(sequence)

for j in range(len(propensity)):
    if(freq_mat[j]!=0):
        percen_hel_res = freq_mat_alpha[j]/freq_mat[j]
        propensity[j] = percen_hel_res/percen_helix
        propensity[j] = round(propensity[j],2)

print("The propensity of amino acid are:")
print("Alanine:",propensity[0])
print("Cysteine:",propensity[2])
print("Aspartic acid:",propensity[3])
print("Glutamic acid:",propensity[4])
print("Phenylalanine:",propensity[5])
print("Glycine:",propensity[6])
print("Histidine:",propensity[7])
print("Isoleucine:",propensity[8])
print("Lysine:",propensity[10])
print("Leucine:",propensity[11])
print("Methionine:",propensity[12])
print("Asparagine:",propensity[13])
print("Proline:",propensity[15])
print("Glutamine:",propensity[16])
print("Arginine:",propensity[17])
print("Serine:",propensity[18])
print("Threonine:",propensity[19])
print("Valine:",propensity[21])
print("Tryptophan:",propensity[22])
print("Tyrosine:",propensity[24])
print(" ")
