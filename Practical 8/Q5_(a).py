
file = open("Q4.fasta")
sequences = file.readlines()
file.close()

match_string1 = "[SV]-T-[VT]-[DERK](2)-{IL}"

print("Finding matches for pattern (a):",match_string1)
print(" ")

def seq_create(seq,n):
    new_seq = ""
    for i in range(n,n+6):
        new_seq = new_seq + seq[i]
    return new_seq

for i in range(1,len(sequences),2):
    header = sequences[i-1]
    seq = sequences[i]
    for j in range(0,len(seq)-6):
        count = 0
        check_seq = seq_create(seq,j)
        if((check_seq[0]=='S') or (check_seq[0]=='V')):
            count+=1
        if(check_seq[1]=='T'):
            count+=1
        if((check_seq[2]=='V') or (check_seq[2]=='T')):
            count+=1
        if((check_seq[3]=='D') or (check_seq[3]=='E') or (check_seq[3]=='R') or (check_seq[3]=='K')):
            count+=1
        if((check_seq[4]=='D') or (check_seq[4]=='E') or (check_seq[4]=='R') or (check_seq[4]=='K')):
            count+=1
        if((check_seq[5]!='I') and (check_seq[5]!='L')):
            count+=1
        if(count==6):
            print(header[:-1])
            print(check_seq)
            print("Position:",j)
            print(" ")
            print(" ")
