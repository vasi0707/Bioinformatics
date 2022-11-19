import numpy as np

#given sequences
seq1 = "ACAGTCGAACG"
seq2 = "ACCGTCCG"

#given scores
match_score = 2
mismatch_score = -1
gap_penalty = -2

#initialisng a matrix of 0 of size-length of seq1+1 and length of seq2+1
mat = np.zeros((len(seq2)+1,len(seq1)+1))
#filling gap penalties in first row and column
for i in range(1,len(seq1)+1):
    mat[0][i]=mat[0][i-1] + gap_penalty
for j in range(1,len(seq2)+1):
    mat[j][0]=mat[j-1][0] + gap_penalty

#function to calculate left score
def left_score(matrix,n,m):
    a = matrix[n][m-1] + gap_penalty
    return a
#function to calculate top score
def top_score(matrix,n,m):
    b = matrix[n-1][m] + gap_penalty
    return b
#function to calculate diaagonal score
def diag_score(matrix,n,m):
    if seq2[n-1]==seq1[m-1]:
        c = matrix[n-1][m-1] + match_score
    else:
        c = matrix[n-1][m-1] + mismatch_score
    return c

#filling the matrix using formula: maximum of top,left,diagonal score
for i in range(1,len(seq2)+1):
    for j in range(1,len(seq1)+1):
        a=left_score(mat,i,j)
        b=top_score(mat,i,j)
        c=diag_score(mat,i,j)
        mat[i][j] = max(a,b,c)

x=len(seq2)
y=len(seq1)
#initialising traceback matrix
traceback_mat=[]

#tracing back 
while(x>=0):
    while(y>=0):
        if(seq2[x-1]==seq1[y-1]):
            traceback_mat.append(1)
            x=x-1
            y=y-1
        else:
            if(mat[x-1][y-1]>=mat[x-1][y] and mat[x-1][y-1]>=mat[x][y-1]):
                traceback_mat.append(0)
                x=x-1
                y=y-1
            elif(mat[x][y-1]>=mat[x-1][y] and mat[x][y-1]>mat[x-1][y-1]):
                traceback_mat.append(-1)
                y=y-1
            elif(mat[x-1][y]>mat[x][y-1] and mat[x-1][y]>mat[x-1][y-1]):
                traceback_mat.append(-2)
                x=x-1

#reversing the traceback matrix            
traceback_mat = traceback_mat[::-1]
#initialsing new akignment sequence
align_seq1=""
align_seq2=""
#creating aligned sequence using traceback matrix
for i in range(1,len(traceback_mat)):
    if(traceback_mat[i]==1):
        align_seq1=align_seq1+seq1[i-1]
        align_seq2=align_seq2+seq1[i-1]
    elif(traceback_mat[i]==0):
        align_seq1=align_seq1+seq1[i-1]
        align_seq2=align_seq2+seq2[i-1]
    elif(traceback_mat[i]==-1):
        align_seq1=align_seq1+seq1[i-1]
        align_seq2=align_seq2+"-"
    else:
        align_seq1=align_seq1+"-"
        align_seq2=align_seq2+seq2[i-1]

#printing the values
print("The aligned sequence 1 is:")
print(align_seq1)
print("The aligned sequence 2 is:")
print(align_seq2)
print("The partial alignment matrix is:")
print(mat)

