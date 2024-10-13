import sys
fastafile = sys.argv[1] 
fasta={}
with open(fastafile) as file:
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
    motif = bases
    motif = input("Enter the motif you want to find:").upper().replace(" ", "")
    motiflist = [*motif] 
    supermotif = list(set(motiflist)) 
    if len(motif) < 5:
        print("The motif must have at least 5 base pairs.")
        Value = False 
    else:
        Value = True 
        if any(x not in bases for x in supermotif):
                print("The motif must only contain the IUPAC nucleotide bases.") 
                Value = False
        else:
            Value = True 
    if Value:
        break                   
for seqs in fasta.values():
    for x in range(len(seqs) - len(motif) + 1):
        if seqs[x: x + len(motif)] == motif:
            frame = (x + 1) % 3 
            if frame == 0:
                frame = -3
            for name in fasta.keys():
                print(f"{name}\t{len(seqs)}\t{x + 1}\t{frame}")
