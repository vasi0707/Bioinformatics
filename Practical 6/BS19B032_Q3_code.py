import numpy as np
import math

total_sequences = int(input("Enter the number of sequences:"))
sequences = []

for i in range(total_sequences):
    sequences.append(input("Enter the multiple alligned sequence:"))

frequency_matrix = np.zeros([27,len(sequences[0])])

for i in range(total_sequences):
    for j in range(len(sequences[0])):
        residue = ord(sequences[i][j]) - 65
        if(sequences[i][j] != '-'):
            frequency_matrix[residue][j] = frequency_matrix[residue][j] + 1
        else:
            frequency_matrix[26][j] = frequency_matrix[26][j] + 1

frequency_matrix = frequency_matrix/(total_sequences)
print("Entropy measures")

for i in range(len(sequences[0])):
    score = 0
    for j in range(27):
        if(frequency_matrix[j][i] != 0):
            score = score + (frequency_matrix[j][i]*(math.log(frequency_matrix[j][i])))
    print("The conservation score(ENTROPY) at position " + str(i+1) + " is: " + str(score))

freq = []
for i in range(27):
    n = 0
    for j in range(len(sequences[0])):
        n = n + frequency_matrix[i][j]
    freq.append(n)

print("Variance measures")
for i in range(len(sequences[0])):
    score = 0
    for j in range(27):
        score = score + (frequency_matrix[j][i]-freq[j])*(frequency_matrix[j][i]-freq[j])
    score = math.sqrt(score)
    print("The conservation score(VARIANCE) at position " + str(i+1) + " is: " + str(score))
