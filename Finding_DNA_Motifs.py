import sys

fasta={}

with open(sys.argv[1]) as file:
    for line in file:
        line=line.strip()
        if not line:
            continue
        if line.startswith(">"):
            seq_names=line[1:]
            if seq_names not in fasta:
                fasta[seq_names]=""
            continue
        sequences=line
        fasta[seq_names]+=sequences
        
        
while True: 
    bases = ["A", "T", "C", "G"] 
    motif = input("Enter the motif you want to find:").upper().replace(" ", "")
    check_chars = all(char in bases for char in motif)
    if len(motif) < 5:
        print("The motif must have at least 5 base pairs.")
        Value = False 
    else:
        Value = True 
        if check_chars == False:
                print("The motif must only contain the IUPAC nucleotide bases.") 
                Value = False
        else:
            Value = True 
    if Value:
        break   
          
print("Order of values: Sequence_name   Sequence_length Motif_position  Frame\n")     
 
for seqs in fasta.values():
    for x in range(len(seqs) - len(motif) + 1):
        if seqs[x: x + len(motif)] == motif:
            frame = (x + 1) % 3 
            if frame == 0:
                frame = -3
            for name in fasta.keys():
                print(f"{name}\t{len(seqs)}\t{x + 1}\t{frame}")
