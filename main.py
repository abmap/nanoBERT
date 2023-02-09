from transformers import pipeline, RobertaTokenizer

# Initialise the tokenizer and the unmasker
tokenizer = RobertaTokenizer.from_pretrained("antibody-tokenizer", return_tensors="pt")

# Reduce the number of predicted residues from 20 to gain speed
unmasker = pipeline('fill-mask', model="nanoBERT/nanoBERT", tokenizer=tokenizer, top_k=20)

# Predict the residue probability at one or more masked positions
seq = "QLVQSGPEVKKP<mask>ASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS"

residueProbability = unmasker(seq)

# Print residue probabilities
for probability in residueProbability:
    print(probability)
