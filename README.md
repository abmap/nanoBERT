# nanoBERT
---

<div align="center">    
 
# nanoBERT: A model for gene agnostic navigation of the nanobody space 

[![DOI:10.1101/2022.01.20.477061](http://img.shields.io/badge/DOI-10.1101/2022.01.20.477061-B31B1B.svg)](https://doi.org/10.1101/2022.01.20.477061)

</div>

**Motivation:** Nanobodies are a subclass of immunoglobulins, whose binding site consists of only one peptide chain, bestowing favorable biophysical properties. In 2018, first nanobody therapy was approved, paving the way for further clinical applications of this format. Further development of nanobody-based therapeutics could be streamlined by computational methods streamlining this format. One of such methods is positional prediction 
**Results**: Here we present nanoBERT, a BERT-based nanobody specific method to predict amino acids in a specific position in a query nanobody. We demonstrate the need to develop such machine learning based method as opposed to simple positional statistics as appropriate genetic reference is not available. We benchmark nanoBERT with respect to a human-based language model, demonstrating the benefit for domain-specific language models. nanoBERT should help nanobody engineers to select naturally plausible nanobody mutations to streamline therapeutic development in this format. 


-----------

# Install nanoBERT

nanoBERT is freely available and can be employed via the Hugging Face framwork 

~~~.sh
    hugface install nanobert
~~~

----------

# use cases
nanoBERT can be used, as is, for **residue prediction**. Or it can be **extended** for buildig nanobody classification models. 

## Nanobody residue prediction

Restoration of antibody sequences can be done using the "restore" mode as seen below.

```{r, engine='python', count_lines}
import ablang

heavy_ablang = ablang.pretrained("heavy") # Use "light" if you are working with light chains
heavy_ablang.freeze()


seqs = [
    'EV*LVESGPGLVQPGKSLRLSCVASGFTFSGYGMHWVRQAPGKGLEWIALIIYDESNKYYADSVKGRFTISRDNSKNTLYLQMSSLRAEDTAVFYCAKVKFYDPTAPNDYWGQGTLVTVSS',
    '*************PGKSLRLSCVASGFTFSGYGMHWVRQAPGKGLEWIALIIYDESNK*YADSVKGRFTISRDNSKNTLYLQMSSLRAEDTAVFYCAKVKFYDPTAPNDYWGQGTL*****',
]

heavy_ablang(seqs, mode='restore')

```

The output of the above is seen below.

```console
array(['EVQLVESGPGLVQPGKSLRLSCVASGFTFSGYGMHWVRQAPGKGLEWIALIIYDESNKYYADSVKGRFTISRDNSKNTLYLQMSSLRAEDTAVFYCAKVKFYDPTAPNDYWGQGTLVTVSS',
       'QVQLVESGGGVVQPGKSLRLSCVASGFTFSGYGMHWVRQAPGKGLEWIALIIYDESNKYYADSVKGRFTISRDNSKNTLYLQMSSLRAEDTAVFYCAKVKFYDPTAPNDYWGQGTLVTVSS'],
      dtype='<U121')
```
-----

## Extending nanoBERT
nanoBERT vas build on the 



### Citation   
```
tba
```  
