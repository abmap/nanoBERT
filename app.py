# pip install streamlit
import pandas as pd
import streamlit as st
from transformers import RobertaTokenizer, pipeline

ALLOWED_CHARS = set('ACDEFGHIKLMNPQRSTVWY*')


def validate_input_seq(seq: str):
    seq_chars = set(seq.upper())
    if not seq_chars.issubset(ALLOWED_CHARS):
        disallowed_chars = ''.join(seq_chars - ALLOWED_CHARS)
        st.error(f'Incorrect chars: "{disallowed_chars}"!')
        st.stop()
    num_placeholder = seq.count('*')
    if num_placeholder != 1:
        st.error('Please use exactly one * placeholder!')
        st.stop()


@st.cache_resource
def get_unmasker():
    tokenizer = RobertaTokenizer.from_pretrained("antibody-tokenizer", return_tensors="pt")
    # Reduce the number of predicted residues from 20 to gain speed
    unmasker = pipeline('fill-mask', model="nanoBERT/nanoBERT", tokenizer=tokenizer, top_k=20)
    return unmasker


def calculate_probabilities(seq: str):
    unmasker = get_unmasker()
    seq_predict = seq.replace('*', '<mask>')
    # st.write(seq_predict)
    residueProbability = unmasker(seq_predict)
    return residueProbability


st.set_page_config(layout="wide")
st.title('nanoBERT - A model for gene agnostic navigation of the nanobody space')

seq = st.text_input(label='Sequence (Use only AA codes and * as placeholder for prediction)',
                    value='QLVQSGPEVKKP*ASVKVSCKASGYIFNNYGISWVRQAPGQGLEWMGWISTDNGNTNYAQKVQGRVTMTTDTSTSTAYMELRSLRYDDTAVYYCANNWGSYFEHWGQGTLVTVSS')
validate_input_seq(seq)

residueProbability = calculate_probabilities(seq)

df = pd.DataFrame(residueProbability).rename(columns={'token_str': 'aa', 'score': 'probability'}).set_index('aa').drop(
    columns=['token'])
df_style = df.style. \
    format('{:.3f}', subset=['probability']). \
    bar(subset=['probability'], vmin=0, vmax=1)
st.write(df_style.to_html(escape=False), unsafe_allow_html=True)
