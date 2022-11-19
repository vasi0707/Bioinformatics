seq=input("Enter your DNA sequence:")       #taking input sequence
comp_seq=""

for i in range(len(seq)):
    if(seq[i]=='A'):
        comp_seq+='T'            #creating complementary sequence 
    if(seq[i]=='T'):
        comp_seq+='A'
    if(seq[i]=='C'):            #A to T; T to A; C to G; G to C
        comp_seq+='G'
    if(seq[i]=='G'):
        comp_seq+='C'

print(comp_seq)
