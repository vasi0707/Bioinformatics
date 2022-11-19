seq=input("Enter your sequence:")
stack_energy=0

for i in range(len(seq)-1):
    if(seq[i]=='A'):
        if(seq[i+1]=='A'):
            stack_energy=stack_energy + (-4)
        if(seq[i+1]=='T'):
            stack_energy=stack_energy + (-7)
        if(seq[i+1]=='C'):
            stack_energy=stack_energy + (-5)
        if(seq[i+1]=='G'):
            stack_energy=stack_energy + (-11)
    if(seq[i]=='T'):
        if(seq[i+1]=='A'):
            stack_energy=stack_energy + (-7)
        if(seq[i+1]=='T'):
            stack_energy=stack_energy + (-2)
        if(seq[i+1]=='C'):
            stack_energy=stack_energy + (-3)
        if(seq[i+1]=='G'):
            stack_energy=stack_energy + (-4)
    if(seq[i]=='C'):
        if(seq[i+1]=='A'):
            stack_energy=stack_energy + (-9)
        if(seq[i+1]=='T'):
            stack_energy=stack_energy + (-5)
        if(seq[i+1]=='C'):
            stack_energy=stack_energy + (-6)
        if(seq[i+1]=='G'):
            stack_energy=stack_energy + (-7)
    if(seq[i]=='G'):
        if(seq[i+1]=='A'):
            stack_energy=stack_energy + (-9)
        if(seq[i+1]=='T'):
            stack_energy=stack_energy + (-6)
        if(seq[i+1]=='C'):
            stack_energy=stack_energy + (-4)
        if(seq[i+1]=='G'):
            stack_energy=stack_energy + (11)

avg_stack_energy=stack_energy/(len(seq)-1)

print("The average stacking energy of given sequence is:",avg_stack_energy)
