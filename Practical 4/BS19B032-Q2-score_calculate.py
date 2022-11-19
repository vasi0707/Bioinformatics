#getting sequence input from user
seq1 = input("Enter your sequence 1:")
seq2 = input("Enter your sequence 2:")

match_score = 1
mismatch_score = 0
origination_penalty = -2
length_penalty = -1

#function to find number of gaps
def gap_find(seq):
    gap_count=0
    flag=0
    for i in range(len(seq)):
        if(seq[i]=='-'):
            if(flag==0):
                gap_count=gap_count+1
                flag=1
        else:
            flag=0
    return gap_count

#function to count total gaps(including consecutive gaps)
def gap_num(seq):
    gaps = 0
    for i in range(len(seq)):
        if(seq[i]=='-'):
            gaps=gaps+1
    return gaps

#initialising total match and mismatch counts to 0
match=0
mismatch=0

#calculating length penalty(including the gaps)
if(len(seq1)==len(seq2)):
    length_diff=abs(gap_num(seq1)-gap_num(seq2))
else:
    length_diff=abs(abs(len(seq1)-len(seq2)) - abs(gap_num(seq1)-gap_num(seq2)))

for i in range(len(seq1)):
    if(seq1[i]==seq2[i]):
        match=match+1
    else:
        mismatch=mismatch+1

#calculating gap penalty
gap_count = gap_find(seq1) + gap_find(seq2)

#calculating total score for alignment with given match scores
score = match*match_score + mismatch*mismatch_score + gap_count*origination_penalty + length_diff*length_penalty

print("The score for given sequence alignments is:",score)
