#importing required libraries
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as pyplt
#given sequences
human_seq = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"
chick_seq = "MVHWTAEEKQLITGLWGKVNVAECGAEALARLLIVYPWTQRFFASFGNLSSPTAILGNPMVRAHGKKVLTSFGDAVKNLDNIKNTFSQLSELHCDKLHVDPENFRLLGDILIIVLAAHFSKDFTPECQAAWQKLVRVVAHALARKYH"

#function to check matches between given sequences
def seq_check(seq1,seq2):
    mat=np.zeros((len(seq1),len(seq2)))
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if(seq1[i]==seq2[j]):
                if(i==j):
                    mat[i][j]=2
                else:
                    mat[i][j]=1
    return mat

#function to print matched parts of seuence
def align_seq(seq1,seq2):
    seq = ""
    for i in range(len(seq1)):
        if(seq1[i]==seq2[i]):
            seq = seq + seq1[i]
        else:
            seq = seq + "-"
    return seq

aligned_seq = align_seq(human_seq,chick_seq)
print(aligned_seq)
#plotting the graph
mat = seq_check(human_seq,chick_seq)
pyplt.imshow(mat)
pyplt.show()

