human_seq='MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH'
chick_seq='MVHWTAEEKQLITGLWGKVNVAECGAEALARLLIVYPWTQRFFASFGNLSSPTAILGNPMVRAHGKKVLTSFGDAVKNLDNIKNTFSQLSELHCDKLHVDPENFRLLGDILIIVLAAHFSKDFTPECQAAWQKLVRVVAHALARKYH'

total_identical = 0
total_similarity = 0
gap1 = 0
gap2 = 0

for i in range(len(human_seq)):
    if(human_seq[i]=='-'):
        gap1 = gap1 + 1
    if(chick_seq[i]=='-'):
        gap2 = gap2 + 1
    if(human_seq[i]==chick_seq[i]):
        total_identical = total_identical + 1
    elif((human_seq[i]=='A') or (human_seq[i]=='I') or (human_seq[i]=='L') or (human_seq[i]=='M') or (human_seq[i]=='F') or (human_seq[i]=='W') or (human_seq[i]=='V')):
        if((chick_seq[i]=='A') or (chick_seq[i]=='I') or (chick_seq[i]=='L') or (chick_seq[i]=='M') or (chick_seq[i]=='F') or (chick_seq[i]=='W') or (chick_seq[i]=='V')):
            total_similarity = total_similarity + 1
    elif((human_seq[i]=='K') or (human_seq[i]=='R')):
        if((human_seq[i]=='K') or (human_seq[i]=='R')):
            total_similarity = total_similarity + 1
    elif((human_seq[i]=='S') or (human_seq[i]=='T')):
        if((human_seq[i]=='S') or (human_seq[i]=='T')):
            total_similarity = total_similarity + 1
    elif((human_seq[i]=='H') or (human_seq[i]=='Y')):
        if((human_seq[i]=='H') or (human_seq[i]=='Y')):
            total_similarity = total_similarity + 1

sequence_identity = (total_identical/len(human_seq))*100
print("The sequence identity of given sequences is:",sequence_identity)
similarity = ((total_identical+total_similarity)/len(human_seq))*100
print("The similarity of given sequences is:",similarity)
gap_percentage1 = (gap1/len(human_seq))*100
gap_percentage2 = (gap2/len(chick_seq))*100
print("The gap percentage of human sequence is:",gap1)
print("The gap percentage of chick sequence is:",gap2)
