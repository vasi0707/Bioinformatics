seq=input("Enter your DNA sequence:")
mrna_seq=""
protein=""

for i in range(len(seq)):
    if(seq[i]=='T'):
        mrna_seq+='U'
    else:
        mrna_seq+=seq[i]

length=0
if(len(mrna_seq)%3==0):
    length=len(mrna_seq)
elif(len(mrna_seq)%3==1):
    length=len(mrna_seq)-1
else:
    length=len(mrna_seq)-2

for i in range(0,length,3):
    if(mrna_seq[i]=='A'):
        if(mrna_seq[i+1]=='A'):
            if(mrna_seq[i+2]=='A'):
                protein+='K'
            if(mrna_seq[i+2]=='U'):
                protein+='N'
            if(mrna_seq[i+2]=='C'):
                protein+='N'
            if(mrna_seq[i+2]=='G'):
                protein+='K'
        if(mrna_seq[i+1]=='U'):
            if(mrna_seq[i+2]=='A'):
                protein+='I'
            if(mrna_seq[i+2]=='U'):
                protein+='I'
            if(mrna_seq[i+2]=='C'):
                protein+='I'
            if(mrna_seq[i+2]=='G'):
                protein+='M'
        if(mrna_seq[i+1]=='C'):
            if(mrna_seq[i+2]=='A'):
                protein+='T'
            if(mrna_seq[i+2]=='U'):
                protein+='T'
            if(mrna_seq[i+2]=='C'):
                protein+='T'
            if(mrna_seq[i+2]=='G'):
                protein+='T'
        if(mrna_seq[i+1]=='G'):
            if(mrna_seq[i+2]=='A'):
                protein+='R'
            if(mrna_seq[i+2]=='U'):
                protein+='S'
            if(mrna_seq[i+2]=='C'):
                protein+='S'
            if(mrna_seq[i+2]=='G'):
                protein+='R'
    if(mrna_seq[i]=='U'):
        if(mrna_seq[i+1]=='A'):
            if(mrna_seq[i+2]=='A'):
                protein+='*'
            if(mrna_seq[i+2]=='U'):
                protein+='Y'
            if(mrna_seq[i+2]=='C'):
                protein+='Y'
            if(mrna_seq[i+2]=='G'):
                protein+='*'
        if(mrna_seq[i+1]=='U'):
            if(mrna_seq[i+2]=='A'):
                protein+='J'
            if(mrna_seq[i+2]=='U'):
                protein+='F'
            if(mrna_seq[i+2]=='C'):
                protein+='F'
            if(mrna_seq[i+2]=='G'):
                protein+='J'
        if(mrna_seq[i+1]=='C'):
            if(mrna_seq[i+2]=='A'):
                protein+='S'
            if(mrna_seq[i+2]=='U'):
                protein+='S'
            if(mrna_seq[i+2]=='C'):
                protein+='S'
            if(mrna_seq[i+2]=='G'):
                protein+='S'
        if(mrna_seq[i+1]=='G'):
            if(mrna_seq[i+2]=='A'):
                protein+='*'
            if(mrna_seq[i+2]=='U'):
                protein+='C'
            if(mrna_seq[i+2]=='C'):
                protein+='C'
            if(mrna_seq[i+2]=='G'):
                protein+='W'
    if(mrna_seq[i]=='C'):
        if(mrna_seq[i+1]=='A'):
            if(mrna_seq[i+2]=='A'):
                protein+='Q'
            if(mrna_seq[i+2]=='U'):
                protein+='H'
            if(mrna_seq[i+2]=='C'):
                protein+='H'
            if(mrna_seq[i+2]=='G'):
                protein+='Q'
        if(mrna_seq[i+1]=='U'):
            if(mrna_seq[i+2]=='A'):
                protein+='L'
            if(mrna_seq[i+2]=='U'):
                protein+='L'
            if(mrna_seq[i+2]=='C'):
                protein+='L'
            if(mrna_seq[i+2]=='G'):
                protein+='L'
        if(mrna_seq[i+1]=='C'):
            if(mrna_seq[i+2]=='A'):
                protein+='P'
            if(mrna_seq[i+2]=='U'):
                protein+='P'
            if(mrna_seq[i+2]=='C'):
                protein+='P'
            if(mrna_seq[i+2]=='G'):
                protein+='P'
        if(mrna_seq[i+1]=='G'):
            if(mrna_seq[i+2]=='A'):
                protein+='R'
            if(mrna_seq[i+2]=='U'):
                protein+='R'
            if(mrna_seq[i+2]=='C'):
                protein+='R'
            if(mrna_seq[i+2]=='G'):
                protein+='R'
    if(mrna_seq[i]=='G'):
        if(mrna_seq[i+1]=='A'):
            if(mrna_seq[i+2]=='A'):
                protein+='E'
            if(mrna_seq[i+2]=='U'):
                protein+='D'
            if(mrna_seq[i+2]=='C'):
                protein+='D'
            if(mrna_seq[i+2]=='G'):
                protein+='E'
        if(mrna_seq[i+1]=='U'):
            if(mrna_seq[i+2]=='A'):
                protein+='V'
            if(mrna_seq[i+2]=='U'):
                protein+='V'
            if(mrna_seq[i+2]=='C'):
                protein+='V'
            if(mrna_seq[i+2]=='G'):
                protein+='V'
        if(mrna_seq[i+1]=='C'):
            if(mrna_seq[i+2]=='A'):
                protein+='A'
            if(mrna_seq[i+2]=='U'):
                protein+='A'
            if(mrna_seq[i+2]=='C'):
                protein+='A'
            if(mrna_seq[i+2]=='G'):
                protein+='A'
        if(mrna_seq[i+1]=='G'):
            if(mrna_seq[i+2]=='A'):
                protein+='G'
            if(mrna_seq[i+2]=='U'):
                protein+='G'
            if(mrna_seq[i+2]=='C'):
                protein+='G'
            if(mrna_seq[i+2]=='G'):
                protein+='G'

print(protein)
