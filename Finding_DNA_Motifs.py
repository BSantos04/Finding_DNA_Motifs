import sys

# Define dictionary variable to store the sequences and their respective names from the FASTA file
fasta={}

# Open the file and separate the sequences from their respective names, storing both in the dictionary previously defined
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
        
# Create an interactive input for the motif to ensure that the code will only run if the motif complies with the established conditions
while True: 
    bases = ["A", "T", "C", "G"] 
    motif = input("Enter the motif you want to find:").upper().replace(" ", "")
    check_chars = all(char in bases for char in motif)
    if len(motif) < 5:
        print("The motif must have at least 5 base pairs.")
        Value = False 
    else:
        if check_chars == False:
            print("The motif must only contain the IUPAC nucleotide bases.") 
            Value = False
        else:
            Value = True 
    if Value:
        break   
# Print a message to indicate the order of the results that will be displayed
print("Sequence_name   Sequence_length Motif_position  Frame\n")     

# Get the results of the query by searching in every frame of the sequences
for seqs in fasta.values():
    for x in range(len(seqs) - len(motif) + 1):
        if seqs[x: x + len(motif)] == motif:
            frame = (x + 1) % 3 
            if frame == 0:
                frame = -3
            for name in fasta.keys():
                print(f"{name}\t{len(seqs)}\t{x + 1}\t{frame}")
