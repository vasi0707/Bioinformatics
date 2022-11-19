seq=input("Enter your sequence:")
check_str=input("Enter the string to search:")
matches=0

for i in range(len(seq)-len(check_str)+1):
    count=0
    for j in range(len(check_str)):
        if(seq[i+j]==check_str[j]):
            count=count+1
    if(count==len(check_str)):
        matches=matches+1
        print("Match location:",i)
print("Total matches:",matches)
