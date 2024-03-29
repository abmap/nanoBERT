# nanoBERT
---

# nanoBERT: A model for gene agnostic navigation of the nanobody space

**Motivation:** Nanobodies are a subclass of immunoglobulins, whose binding site consists of only one peptide chain,
bestowing favorable biophysical properties. In 2018, first nanobody therapy was approved, paving the way for further
clinical applications of this format. Further development of nanobody-based therapeutics could be streamlined by
computational methods streamlining this format. One of such methods is positional prediction
**Results**: Here we present nanoBERT, a BERT-based nanobody specific method to predict amino acids in a specific
position in a query nanobody. We demonstrate the need to develop such machine learning based method as opposed to simple
positional statistics as appropriate genetic reference is not available. We benchmark nanoBERT with respect to a
human-based language model, demonstrating the benefit for domain-specific language models. nanoBERT should help nanobody
engineers to select naturally plausible nanobody mutations to streamline therapeutic development in this format.


-----------

# Install nanoBERT

nanoBERT is build using the Hugging Face framwork, and can be cloned from the Hugging Face Hub.

```
git clone https://huggingface.co/abmap/nanoBERT
```

----------

# Use cases

nanoBERT can be used, as is, for **residue prediction**. Or it can be **extended** with additional layers to build
nanobody classification models.

## Residue prediction

Below is a minimal example of how to loade the model and predict or validate a residue on a masked position.

```
! pip install transformers torch
! git clone https://huggingface.co/abmap/nanoBERT

import torch
from transformers import pipeline, RobertaTokenizer

# Initialise the tokenizer and the unmasker
tokenizer = RobertaTokenizer.from_pretrained("antibody-tokenizer", return_tensors="pt")

# Reduce the number of predicted residues from 20 to gain speed
unmasker = pipeline('fill-mask', model="nanoBERT/nanoBERT", tokenizer=tokenizer, top_k = 20)
#unmasker = pipeline('fill-mask', model="nanoBERT/nanoDist18", tokenizer=tokenizer, top_k = 20) # using the nanoDist18 variant 

# Predict the residue probability at one or more masked positions
seq = "QLVQSGPEVKKP<mask>ASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS"

residueProbability = unmasker(seq)

# Print residue probabilities 
for probability in residueProbability:
    print(probability))
```

This will return the `top_k` most probable residues at the masked position.

```console
{'score': 0.9021952748298645, 'token': 10, 'token_str': 'G', 'sequence': 'QLVQSGPEVKKPGASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS'}
{'score': 0.025880739092826843, 'token': 19, 'token_str': 'R', 'sequence': 'QLVQSGPEVKKPRASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS'}
{'score': 0.024441681802272797, 'token': 23, 'token_str': 'W', 'sequence': 'QLVQSGPEVKKPWASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS'}
{'score': 0.012200706638395786, 'token': 8, 'token_str': 'E', 'sequence': 'QLVQSGPEVKKPEASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS'}
{'score': 0.010569128207862377, 'token': 5, 'token_str': 'A', 'sequence': 'QLVQSGPEVKKPAASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS'}
{'score': 0.009906540624797344, 'token': 22, 'token_str': 'V', 'sequence': 'QLVQSGPEVKKPVASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS'}
{'score': 0.0032364593353122473, 'token': 6, 'token_str': 'C', 'sequence': 'QLVQSGPEVKKPCASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS'}
{'score': 0.002486324869096279, 'token': 20, 'token_str': 'S', 'sequence': 'QLVQSGPEVKKPSASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS'}
{'score': 0.0019146149279549718, 'token': 17, 'token_str': 'P', 'sequence': 'QLVQSGPEVKKPPASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS'}
{'score': 0.0016250761691480875, 'token': 14, 'token_str': 'L', 'sequence': 'QLVQSGPEVKKPLASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS'}
{'score': 0.0012130311224609613, 'token': 9, 'token_str': 'F', 'sequence': 'QLVQSGPEVKKPFASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS'}
{'score': 0.0010787055362015963, 'token': 7, 'token_str': 'D', 'sequence': 'QLVQSGPEVKKPDASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS'}
{'score': 0.0008880678215064108, 'token': 18, 'token_str': 'Q', 'sequence': 'QLVQSGPEVKKPQASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS'}
{'score': 0.0006741221877746284, 'token': 21, 'token_str': 'T', 'sequence': 'QLVQSGPEVKKPTASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS'}
{'score': 0.0005145570612512529, 'token': 13, 'token_str': 'K', 'sequence': 'QLVQSGPEVKKPKASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS'}
{'score': 0.000412171269999817, 'token': 24, 'token_str': 'Y', 'sequence': 'QLVQSGPEVKKPYASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS'}
{'score': 0.00031191640300676227, 'token': 15, 'token_str': 'M', 'sequence': 'QLVQSGPEVKKPMASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS'}
{'score': 0.00022084052034188062, 'token': 12, 'token_str': 'I', 'sequence': 'QLVQSGPEVKKPIASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS'}
{'score': 0.00014110600750427693, 'token': 16, 'token_str': 'N', 'sequence': 'QLVQSGPEVKKPNASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS'}
{'score': 8.882807742338628e-05, 'token': 11, 'token_str': 'H', 'sequence': 'QLVQSGPEVKKPHASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS'}
```
-----

## Extending nanoBERT
nanoBERT was built on the Hugging Face framework and can be extended to serve as pretrained basis for a sequence
classification. It can also be finetuned to predict residues in a specific context. Refer to the documentation on https://huggingface.co/docs/transformers/index

### Citation

```
tba
```  
