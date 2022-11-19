
file = open("Q4.fasta")
sequences = file.readlines()
file.close()

match_string2 = "[FILV]Qxxx{RK}Gxxx[RK]xx[FILVWY]"

print("Finding matches for pattern (a):",match_string2)
print(" ")

def seq_create(seq,n):
    new_seq = ""
    for i in range(n,n+14):
        new_seq = new_seq + seq[i]
    return new_seq

for i in range(1,len(sequences),2):
    header = sequences[i-1]
    seq = sequences[i]
    for j in range(0,len(seq)-14):
        count = 0
        check_seq = seq_create(seq,j)
        if((check_seq[0]=='F') or (check_seq[0]=='I') or (check_seq[0]=='V') or (check_seq[0]=='L')):
            count+=1
        if(check_seq[1]=='Q'):
            count+=1
        if((check_seq[5]!='R') and (check_seq[5]!='K')):
            count+=1
        if(check_seq[6]=='G'):
            count+=1
        if((check_seq[10]=='R') or (check_seq[10]=='K')):
            count+=1
        if((check_seq[13]=='F') or (check_seq[13]=='I') or (check_seq[13]=='V') or (check_seq[13]=='L') or (check_seq[13]=='W') or (check_seq[13]=='Y')):
            count+=1
        if(count==6):
            print(header[:-1])
            print(check_seq)
            print("Position:",j)
            print(" ")
            print(" ")
