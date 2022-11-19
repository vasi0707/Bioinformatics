import numpy as np
import math

p_alpha = [1.53,0,0.77,0.98,1.53,1.12,0.53,1.24,1.00,0,1.07,1.34,1.20,0.73,0,0.59,1.17,0.79,0.79,0.82,0,1.14,1.14,0,0.61,0]
p_beta = [0.97,0,1.30,0.80,0.26,1.28,0.81,0.71,1.60,0,0.74,1.22,1.67,0.65,0,0.62,1.23,0.90,0.72,1.20,0,1.65,1.19,0,1.29,0]

seq = "KVFGRCELAAAMKRHGLDNYRGYSLGNWVCAAKFESNFNTQATNRNTDGSTDYGILQINSRWWCNDGRTPGSRNLCNIPCSALLSSDITASVNCAKKIVSDGNGMNAWVAWRNRCKGTDVQAWIRGCRL"

def create_seq1(seq,n):
    new_seq = ""
    for i in range(n,n+6):
        new_seq = new_seq + seq[i]
    return new_seq

def create_seq2(seq,n):
    new_seq = ""
    for i in range(n,n+5):
        new_seq = new_seq + seq[i]
    return new_seq

def create_seq3(seq,n):
    new_seq = ""
    for i in range(n,n+4):
        new_seq = new_seq + seq[i]
    return new_seq

def create_seq4(seq,i,j):
    new_seq = ""
    for k in range(i,j+1):
        new_seq = new_seq + seq[k]
    return new_seq

def find_a(seq):
    a = 0
    for j in range(len(seq)):
        res = ord(seq[j]) - 65
        if(p_alpha[res]>1.07):
            a = a + 1
        elif((p_alpha[res]<1.12) and (p_alpha[res]>0.98)):
            a = a + 0.5
        elif((p_alpha[res]<1.00) and (p_alpha[res]>0.73)):
            a = a + 0
        else:
            a = a - 1
    return a

def find_b(seq):
    b = 0
    for j in range(len(seq)):
        res = ord(seq[j]) - 65
        if(p_beta[res]>0.97):
            b = b + 1
        elif(p_beta[res]==0.97):
            b = b + 0.5
        elif((p_beta[res]<0.97) and (p_beta[res]>0.74)):
            b = b + 0
        else:
            b = b - 1
    return b

def find_val1(seq):
    val = 0
    for k in range(4):
        res1 = ord(seq[k]) - 65
        val = val + p_alpha[res1]
    return val

def find_val2(seq):
    val = 0
    for k in range(4):
        res1 = ord(seq[k]) - 65
        val = val + p_beta[res1]
    return val

def seq_print(seq,seq1,seq2):
    pr_seq = ""
    if(len(seq2)>0):
        pr_seq = pr_seq + seq2[0]
        if(len(seq2)>1):
            for i in range(1,len(seq2)):
                s = seq2[i]
                pr_seq = s[0] + pr_seq
    pr_seq = pr_seq + seq
    if(len(seq1)>0):
        pr_seq = pr_seq + seq1[0]
        if(len(seq1)>1):
            for j in range(1,len(seq1)):
                s1 = seq1[j]
                pr_seq = pr_seq + s1[len(s1)-1]
    return pr_seq

helix = []
i = 0
print("The Alpha Helix sequences are:")

while(i<(len(seq)-5)):
    query_seq = create_seq1(seq,i)
    a = find_a(query_seq)
    seq1 = []
    seq2 = []
    if(a>=4):
        front = i+6
        back = i-1
        val1 = 4
        val2 = 4
        while(val1>=4):
            f_s = create_seq3(seq,front)
            val1 = find_val1(f_s)
            if(val1>=4):
                front = front + 1
                seq1.append(f_s)
            else:
                break
        while(val2>=4):
            b_s = create_seq4(seq,back-3,back)
            val2 = find_val1(b_s)
            if(val2>=4):
                back = back - 1
                seq2.append(b_s)
            else:
                break
        helix.append(seq_print(query_seq,seq1,seq2))
        print(seq_print(query_seq,seq1,seq2))
        i = i + 5 + (len(seq1)+4)
    i = i + 1
    
strand = []
j = 0
print(" ")
print("The Beta Strand Sequences are:")

while(j<(len(seq)-4)):
    query_seq = create_seq2(seq,j)
    b = find_b(query_seq)
    if(b>3):
        strand.append(query_seq)
    j=j+1

strand_seq = ""

for i in range(len(strand)):
    if(i==0):
        strand_seq = strand_seq + strand[i]
    else:
        s=strand[i]
        s1=strand[i-1]
        if(s[:-1]==s1[1:]):
            strand_seq = strand_seq + s[len(s)-1]
        else:
            strand_seq = strand_seq + "*"
            strand_seq = strand_seq + s

for i in range(len(strand_seq)):
    if(strand_seq[i]!='*'):
        print(strand_seq[i],end="")
    else:
        print(" ")

print("\n")

for i in range(len(strand)):
    x = strand[i]
    for j in range(len(helix)):
        y = helix[j]
        for k in range(len(y)-3):
            ver = y[k:k+5]
            if(x==ver):
                a1 = find_val1(x)
                b1 = find_val2(x)
                if(a1>b1):
                    print("As helix propensity of ",x,end=" ")
                    print("is greater than strand, it is a helical segment")
                else:
                    print("As strand propensity of ",x,end=" ")
                    print("is greater than helix, it is a strand segment")
    
