seq1 = input("Enter your sequence1:")
seq2 = input("Enter your sequence2:")

print("The Matching Pentapeptides are:")
count = 0
while(count<=(len(seq1)-5)):
    pen_seq1 = seq1[count:count+5]
    if pen_seq1 in seq2:
        print(pen_seq1)
        count2 = 0
        freq1 = 1
        freq2 = 0
        print("The frequency of occurence in sequence 1 is:",freq1)
        while(count2<=(len(seq2)-5)):
            check_seq = seq2[count2:count+5]
            if(check_seq == pen_seq1):
                freq2 = freq2 + 1
            count2 = count2 + 1
        print("The frequency of occurence in sequence 2 is:",freq2)
    count = count + 1
